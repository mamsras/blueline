# Gestionnaire de Tâches

Un gestionnaire de tâches basé sur React et Django REST Framework permettant de créer, modifier, et suivre des tâches avec des fonctionnalités comme la gestion des notifications, la planification des tâches, et un support WebSocket.

## Fonctionnalités

- **Gestion des tâches** : Ajout, modification et suppression des tâches.
- **Notifications en temps réel** : Notifications pour les événements liés aux tâches via WebSocket et redis server.
- **Interface utilisateur moderne** : Utilisation de React et Material UI pour une interface intuitive et responsive.
- **Planification des tâches** : Planifiez les tâches avec des dates et heures spécifiques grâce au champ `datetime-local`.
- **Support multi-utilisateurs** : Sécurisé avec l'authentification par jetons.
- **Automatisation** : Cron jobs configurés pour exécuter des tâches périodiques comme l'envoi des notifications de rappels.

---

## Structure du Projet

### Backend
- **Framework** : Django REST Framework.
- **Notifications** : Géré via Django Channels et WebSocket.
- **Base de données** : SQLite.
- **Planification des tâches** : Intégration de Django-cron pour les tâches automatisées.

### Frontend
- **Framework** : React.js avec React Router.
- **Interface utilisateur** : Conçue avec Material UI et Bootstrap.
- **Gestion des états globaux** : React Context API pour gérer les notifications.

---

## Prérequis

### Backend
- Python 3.8+
- Django 4.2+
- SQLite
- Redis
- `pip install -r requirements.txt`

### Frontend
- Node.js 16+ (LTS recommandé)
- npm ou yarn

---

## Installation et Configuration

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/mamsras/blueline.git

## installation des modules et dépendances

    ## django
    - cd task_manager
    - pip install -r requirements.txt
    - docker-compose up (commande pour installer redis sur docker)
    ## React
    - cd frontend
    - npm install

Puis lancer django avec 'python manage.py runserver' et l'interface React avec 'npm start'