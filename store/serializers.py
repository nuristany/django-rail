from rest_framework import serializers
from .models import Item, Category, ItemImage, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'phone']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'image']


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()
    seller_phone = serializers.SerializerMethodField()
    seller_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'description', 'seller_phone', 'condition', 'category', 'images']

    def get_seller_phone(self, obj):
        # Access the seller's phone number from the associated UserProfile
        if obj.seller:
            return obj.seller.phone
        return None
    
    def get_seller_full_name(self, obj):
        # Combine first_name and last_name into a single field
        if obj.seller:
            return f"{obj.seller.first_name} {obj.seller.last_name}"
        return None

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance, _ = Category.objects.get_or_create(**category_data)
        item_instance = Item.objects.create(category=category_instance, **validated_data)
        return item_instance
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category_serializer = CategorySerializer(instance.category, data=category_data)
            category_serializer.is_valid(raise_exception=True)
            category_serializer.save()
        return super().update(instance, validated_data)
