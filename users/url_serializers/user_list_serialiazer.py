
from users.models import Link
from rest_framework.serializers import ModelSerializer

 class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
