from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from.models import Item, Category, ItemImage, UserProfile
from .serializers import ItemSerializer, CategorySerializer, ItemImageSerializer, UserProfileSerializer
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

# Create your views here.



class UserProfileViewsSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


   
    def get_serializer_context(self):
        return {'request': self.request}
    
  
        

    
class ItemViewSet(ModelViewSet):
     queryset = Item.objects.all()
     queryset = Item.objects.prefetch_related('images').all()
     serializer_class = ItemSerializer
     filter_backends = [DjangoFilterBackend, SearchFilter]
     search_fields = ['title', 'description']
     filterset_fields = ['category_id']
     permission_classes = [IsAuthenticated]


     def get_serializer_context(self):
         return {'request': self.request}
     



class ItemImageViewSet(ModelViewSet):
    serializer_class = ItemImageSerializer

    def get_serializer_context(self):
        return {'item_id': self.kwargs['item_pk']}

    def get_queryset(self):
        return ItemImage.objects.filter(item_id=self.kwargs['item_pk'])