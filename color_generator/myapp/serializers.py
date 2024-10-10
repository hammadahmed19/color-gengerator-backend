from rest_framework import serializers
from .models import Colours

class ColoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = ['id','user_name', 'colours']

    def validate_user_name(self, value):
        if not value:
            raise serializers.ValidationError("User name is required.")
        return value

    def validate_colours(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Colours must be a list.")
        if len(value) != 5:
            raise serializers.ValidationError("Colours array must contain exactly 5 items.")
        return value
