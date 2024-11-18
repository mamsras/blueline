from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user/', views.UserViewsets, basename="user")

urlpatterns = [
    path('admin/', include(router.urls)),
    path('tasks/', views.TaskListCreate.as_view(), name="tasks"),
    path('tasks/<int:pk>', views.TaskRetrieveUpdateDestroy.as_view(), name="update_delete_detail_task"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('tasks/complete/<int:pk>', views.CompleteTask.as_view(), name="complete_task"),
    path('tasks/start/<int:pk>', views.StartTask.as_view(), name="start_task")

]