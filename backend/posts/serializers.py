from rest_framework import serializers
from .models import Blog, Tag

class BlogSerializer(serializers.ModelSerializer):
    read_time = serializers.ReadOnlyField()
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    star_count = serializers.IntegerField(source='stars.count', read_only=True)
    author_username = serializers.ReadOnlyField(source='user.username')
    created_at = serializers.DateTimeField(format="%b %d, %Y", read_only=True)
    cover_image = serializers.ImageField(use_url=True)
    
    tags = serializers.SlugRelatedField(
        many=True, 
        slug_field='name', 
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Blog
        fields = [
            'id', 'slug', 'title', 'summary', 'content', 'cover_image', 
            'author_username', 'created_at', 'updated_at', 
            'read_time', 'like_count', 'star_count', 'category', 'tags'
        ]
        read_only_fields = ['user']

    def to_internal_value(self, data):
        if 'tags' in data and isinstance(data['tags'], list):
            for tag_name in data['tags']:
                Tag.objects.get_or_create(name=tag_name)
        return super().to_internal_value(data)