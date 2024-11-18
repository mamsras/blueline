from models import Task
from django.utils import timezone
from django.utils.timezone import localtime

#une fonction pour marquer les tâches inachevé
def mark_inacheve():
    now = localtime(timezone.now())
    tasks = Task.objects.filter(status = ["À faire", "En cours"], begin_at__date = now.date())
    inach_tasks =[
        task for task in tasks if (task.begin_at+task.duration) < now
    ]

    for task in inach_tasks:
        task.status = "Inachevé"
        task.save()