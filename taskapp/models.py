# from django.db import models
# from django.utils.deconstruct import deconstructible
# import os
# import uuid

import os
import uuid
from django.db import models
from django.utils.deconstruct import deconstructible

NOT_COMPLETE = 'nc'
COMPLETE ='c'
TASK_STATUS_CHOICES = (
    (NOT_COMPLETE, 'Not Completed'),  (COMPLETE, 'Completed')
)



@deconstructible
class GenerateAttachmentPath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        namee, ext =  os.path.splitext(filename)
        path = f'media/tasks/{instance.task.id}/attachments'
        name= f'{instance.id}.{ext}'
        return os.path.join(path,name)


attachment_file_path = GenerateAttachmentPath()



class TaskList(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField( null=True,blank=True)
    house = models.ForeignKey('house.House', on_delete=models.CASCADE, related_name='lists')
    created_by = models.ForeignKey('users.Profile',null=True,blank=True, on_delete=models.SET_NULL,related_name='lists')
    completed_by =models.ForeignKey('users.Profile',null=True,blank=True, on_delete=models.SET_NULL,related_name='completed_task')
    name = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True,)
    status = models.CharField(max_length=2,choices=TASK_STATUS_CHOICES,default=NOT_COMPLETE)

    def __str__(self):
        return f'{self.id} | {self.name}'


class Task(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField( null=True,blank=True)
    task_list = models.ForeignKey('taskapp.TaskList', on_delete=models.CASCADE,related_name='task')
    created_by = models.ForeignKey('users.Profile',null=True,blank=True, on_delete=models.SET_NULL,related_name='created_tasks')
    completed_by =models.ForeignKey('users.Profile',null=True,blank=True, on_delete=models.SET_NULL,related_name='completed_tasks')
    name = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True,)
    status = models.CharField(max_length=2,choices=TASK_STATUS_CHOICES,default=NOT_COMPLETE)

    def __str__(self):
        return f'{self.id} | {self.name}'
    


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    created_on = models.DateTimeField(auto_now_add=True)
    data = models.FileField(upload_to=attachment_file_path)
    task =  models.ForeignKey('taskapp.Task', on_delete=models.CASCADE,related_name='attachment')

    def __str__(self):
        return f'{self.id} | {self.task}' 
