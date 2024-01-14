from background_task import background
from background_task.tasks import Task as ft
from house.models import House
from taskapp.models import  COMPLETE
# from django.contrib.auth.models import User

@background(schedule=10)
def calculate_house_stats():
    for house in House.objects.all():
        total_tasks = 0
        completed_tasks_count = 0
        house_task_lists = house.lists.all()
        for task_list in house_task_lists:
            total_tasks += task_list.tasks.count()
            completed_tasks_count += task_list.tasks.filter(status=COMPLETE).count()
        house.completed_task_count = completed_tasks_count
        house.notcompleted_task_count = total_tasks - completed_tasks_count
        house.save()
