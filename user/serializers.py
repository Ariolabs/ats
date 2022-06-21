from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'is_verified', 'created_at', 'updated_at', 'verified_at', 'premiered_at']
        