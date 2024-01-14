from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .serializer import HouseSerializer
from .models import House
from .permission import IsHouseManagerOrNot


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    permission_classes= [IsHouseManagerOrNot]
    serializer_class = HouseSerializer
    filter_backends =[filters.SearchFilter,DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields =['points','completed_task_count', 'notcompleted_task_count']
    search_fields =['name','description']
    filterset_fields = ['members',]
    
    @action(detail=True, methods=['POST'], name='join', permission_classes=[])
    def join(self, request, pk=None):
        try:
            house =self.get_object()
            user_profile = request.user.profile
            if (user_profile.house == None):
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif (user_profile in house.members.all()):
                return Response({'detail':'Already a member in this house'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail':'Already a member in another house'}, status=status.HTTP_400_BAD_REQUEST)
            

        except Exception as err:
            return Response( status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    @action(detail=True, methods=['POST'], name='leave', permission_classes=[])
    def leave(self, request, pk=None):
        try:
            house =self.get_object()
            user_profile = request.user.profile
            if (user_profile in house.members.all()):
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
          
            else:
                return Response({'detail':'User not a member in this house'}, status=status.HTTP_400_BAD_REQUEST)
            

        except Exception as err:
            return Response( status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             
