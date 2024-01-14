
from rest_framework.routers import DefaultRouter
from .viewset import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet,)
router.register(r'profiles', ProfileViewSet,)
