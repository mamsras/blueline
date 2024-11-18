from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The user's email must be provided")
        if not password:
            raise ValueError("The user must set a password")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self.create_user(email=email, username=username, password=password, **extra_fields)



class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)
    send_email_notification = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"


class Task(models.Model):

    A_FAIRE = 'À faire'
    EN_COURS = 'En cours'
    TERMINE = 'Terminé'
    INACHEVE = 'Inachevé'
    
    STATUS_CHOICES = (
        (A_FAIRE, 'À faire'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        (INACHEVE, 'Inachevé')
    )

    task_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255, default="Pas de déscription")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=A_FAIRE)
    duration = models.DurationField()
    begin_at = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description

    class Meta:
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"