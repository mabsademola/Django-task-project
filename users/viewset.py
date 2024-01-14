from rest_framework import viewsets, mixins
from .models import User  
from .serializer import UserSerializer , ProfileSerializer
from .models import Profile
from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrGetAndPostOnly


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsProfileOwnerOrGetAndPostOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer