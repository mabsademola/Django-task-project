
from rest_framework.routers import DefaultRouter
from .viewset import TaskListViewSet, TaskViewSet,AttachmentViewSet

router = DefaultRouter()
router.register(r'tasklist', TaskListViewSet,)
router.register(r'tasks', TaskViewSet,)
router.register(r'attachment', AttachmentViewSet,)

