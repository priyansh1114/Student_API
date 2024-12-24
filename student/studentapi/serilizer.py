from rest_framework import serializers
from .models import studenapi

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studenapi
        fields = "__all__"