from rest_framework import serializers
from .models import Profile


# convert python models to json
class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner', 
            'created_at', 
            'updated_at', 
            'name', 
            'content', 
            'image'
        ]
