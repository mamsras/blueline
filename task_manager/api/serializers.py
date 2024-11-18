from rest_framework import serializers
from backend.models import Task, User


class TaskSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('task_id', 'createdAt', 'lastUpdate')


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields =('id',)



class TaskToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id']
        read_only_fields = ('description', 'status', 'duration', 'begin_at', 'createdAt', 'lastUpdate',)