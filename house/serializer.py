from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    members = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='user-detail')
    manager = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='user-detail')
    tasklist = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='tasklist-detail', source = 'lists')
 
    class Meta:
        model = House
        fields = ['url','id','image', 'name','created_at', 'manager','description',
                  'tasklist',
                  'members',
                  'points', 'completed_task_count',
                 'notcompleted_task_count'
                 ]
        read_only_fields = ['points', 'completed_task_count', 'notcompleted_task_count']
    