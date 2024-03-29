from django.urls import path
from rest_framework_nested import routers
from . import views

# Create the main router
router = routers.DefaultRouter()
router.register('items', views.ItemViewSet, basename='items')
router.register('category', views.CategoryViewSet)

# Create a nested router for handling images related to items
items_router = routers.NestedDefaultRouter(router, 'items', lookup='item')
items_router.register('images', views.ItemImageViewSet, basename='item-images')

# Combine the URL patterns from both routers
urlpatterns = router.urls + items_router.urls