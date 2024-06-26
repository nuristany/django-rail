from rest_framework import serializers
from django.contrib.auth.models import User

from.models import Item, Category, ItemImage, UserProfile



        
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

    def create(self, validated_data):
        item_id = self.context['item_id']
        return ItemImage.objects.create(item_id=item_id, **validated_data)


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category = serializers.StringRelatedField()
    phone = serializers.SerializerMethodField()
    seller_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'description', 'seller', 'seller_full_name', 'phone', 'condition', 'category', 'images']

    def get_phone(self, obj):
        # Access the contact number from the associated UserProfile
        if obj.seller:
            return obj.seller.phone
        return None
    
    def get_seller_full_name(self, obj):
        # Combine first_name and last_name into a single field
        if obj.seller:
            if obj.seller.first_name and obj.seller.last_name:
                return f"{obj.seller.first_name} {obj.seller.last_name}"
            elif obj.seller.is_superuser:
                return obj.seller.username  # Return username if no first_name and last_name are provided for superuser
        return None

    

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance, _ = Category.objects.get_or_create(id=category_data.id, defaults=category_data.__dict__)
        validated_data['category'] = category_instance
        return Item.objects.create(**validated_data)

    


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    
    # def update(self, instance, validated_data):
    #     category_data = validated_data.pop('category', None)
    #     if category_data:
    #         category_serializer = CategorySerializer(instance.category, data=category_data)
    #         category_serializer.is_valid(raise_exception=True)
    #         category_serializer.save()
    #     return super().update(instance, validated_data)




