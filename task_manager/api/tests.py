from django.test import TestCase

from notify import send_ws_notification
from backend.models import User


def test_notification():
    user = User.objects.get(username="mamsras")
    send_ws_notification(message="vendrapory", user=user)

if __name__ == '__main__':
    test_notification()