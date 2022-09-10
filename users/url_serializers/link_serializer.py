from users.models import Link
from rest_framework.serializers import ModelSerializer


class LinkSerializer(ModelSerializer):
    class Meta:
        model=Link
        fields='__all__'
