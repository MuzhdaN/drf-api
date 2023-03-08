from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        return obj.owner == self.context['request'].user

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at',
            'updated_at', 'title', 'content',
            'image', 'is_owner', 'profile_id', 
            'profile_image', 'image_filter',
        ]
    


    # def create(self, validated_data):
    #     return Post.objects.create(owner=self.context['request'].user, **validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.save()
    #     return instance

