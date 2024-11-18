# tasks.py ou dans une commande Django
from django.utils import timezone
from django.utils.timezone import localtime
from datetime import timedelta
from backend.models import Task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.mail import send_mail
from django.db.models import F
import json
import uuid

def send_ws_notification(message, user):
    notification = {
        "id": str(uuid.uuid4()),  # id unique pour chaque notification
        "message": message,
        "timestamp": str(localtime(timezone.now()))
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user.id}_notifications",
        {
            "type": "send_notification",
            "message": notification,
        }
    )



def send_email(subject:str, message:str, from_email:str, recipient_list:list[str]):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,  # Expéditeur
        recipient_list=recipient_list,  # Destinataire(s)
        fail_silently=False,
    )


#envoyer des notifications aux tâches qui commenceraient dans 5 min
def send_acc_notif ():
    print("La tâche cron pour l'envoi de notification des tâches à faire a commencé")
    maintenant = localtime(timezone.now())
    debut = maintenant + timedelta(minutes=5)

    # Rechercher les tâches qui commencent dans 5 minutes
    taches_a_notifier = Task.objects.filter(begin_at__range=(maintenant, debut))
    print (taches_a_notifier)

    if taches_a_notifier.exists():
        for task in taches_a_notifier:
            user = task.user
            message = f"Bonjour {user.username}, vous avez une tâche à accomplir dans 5 min: '{task.description}'"
            if task.status=="À faire":
                if user.send_email_notification:
                   send_email(subject="Tâche à accomplir", message=message, from_email="", recipient_list=[user.email])
                send_ws_notification(message, user)

    print("Tâche cron términé")


def send_at_notif():
    print("La tâche cron pour l'envoi de notification des tâches à terminer a commencé")

    # Déterminer l'intervalle de temps
    maintenant = localtime(timezone.now())
    borne_inf = maintenant + timedelta(minutes=10)

    # Récupérer les tâches "En cours" et commençant après maintenant
    tasks = Task.objects.filter(status="En cours", begin_at__gte=maintenant)
    

    # Filtrer celles qui se terminent dans l'intervalle
    taches_a_notifier = [
        task for task in tasks
        if (task.begin_at + task.duration) <= borne_inf
    ]

    print(taches_a_notifier)
    # Envoyer les notifications
    for task in taches_a_notifier:
        user = task.user
        try:
            message = f"{user.username}, vous avez une tâche à terminer dans quelques minutes: '{task.description}'"
            if user.send_email_notification:
                send_email(subject="Tâche à terminer", message=message, from_email="", recipient_list=[user.email])
            send_ws_notification(message, user)
        except Exception as e:
            print(f"Erreur lors de l'envoi de notification pour la tâche {task.id}: {e}")

    print("Tâche cron terminée")
