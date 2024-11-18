from django.shortcuts import render
from rest_framework import viewsets
from backend.models import User, Task
from api.serializers import TaskToggleCompleteSerializer, UserSerialiser, TaskSerialiser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import timedelta
# Create your views here.



#une view pour gérer l'inscription et la création de token automatiquement
@api_view(['POST'])
def signup(request):
    try:
        data = JSONParser().parse(request)
        user = User.objects.create_user(
            username = data["username"],
            email = data["email"],
            password = data["password"]
        )
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token':str(token)},status=201)
    except IntegrityError:
        return Response({'error':'username taken. choose another username'},status=400)


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    user = authenticate(
    request,
    username=data['email'],
    password=data['password'])
    user_data = {}
    if user is None:
        return Response({'error':'unable to login. check username and password'},status=400)
    else: # obtenir token
        try:
            token = Token.objects.get(user=user)
            user_data["username"]=user.username
            user_data["email"]=user.email

            return Response({'token':str(token), 'user_data':user_data}, status=201)
        except: # Si l'utilisateur n'as pas de token, créer un
            token = Token.objects.create(user=user)
            return Response({'token':str(token), 'user_data':user_data}, status=201)


class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerialiser
    #queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'createdAt']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user).order_by("begin_at")
    
    def perform_create(self, serializer):
        #définir l'utilisateur liée à la creation de la tâche
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerialiser
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

class StartTask(generics.UpdateAPIView):
    serializer_class = TaskToggleCompleteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.status = "En cours"
        serializer.save()


class CompleteTask(StartTask):
    serializer_class = TaskToggleCompleteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.status = "Terminé"
        serializer.save()