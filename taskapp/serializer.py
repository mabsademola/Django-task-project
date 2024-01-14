# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import  TaskList, Task, Attachment
from house.models import House


class TaskListSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True,many=False, view_name='user-detail')
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(),many=False, view_name='house-detail')
    task = serializers.HyperlinkedRelatedField(read_only=True,many=True, view_name='task-detail')
    class Meta:
        model =TaskList
        fields =['url','id','name','description',
                 'status',
                 'house',
                 'task',
                 'created_by', 
                 'created_on'
                 ]
        read_only_fields = ['created_on', 'status',]
    

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True,many=False, view_name='user-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only=True,many=False, view_name='user-detail')
    task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(),many=False, view_name='tasklist-detail')
    attachment = serializers.HyperlinkedRelatedField(read_only=True,many=True, view_name='attachment-detail')

    def validate_task_list(self, value):
        user_profile = self.context['request'].user.profile
        if value not in user_profile.house.lists.all():
            return serializers.ValidationError('tasklist provided doesnt belong to the house the user is member')
        return value
    def create(self, validated_data):
        user_profile = self.context['request'].user.profile
        task =Task.objects.create(**validated_data)
        task.created_by = user_profile
        task.save()
        return task

   
    class Meta:
        model =Task
        fields =['url','id','name','description',
                 'status',
                 'completed_on',
                 'created_by', 
                 'attachment',
                 'created_on',
                 'completed_by',
                 'task_list',
                 ]
        read_only_fields = ['created_on', 'created_by','completed_by', 'status', 'completed_on']
    


class AttachmentSerializer(serializers.ModelSerializer):
    task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(),many=False, view_name='task-detail')
   
    class Meta:
        model =Attachment
        fields =['url','id',
                 'created_on',
                 'data',
                 'task',
                 ]
        read_only_fields = ['created_on']
    


