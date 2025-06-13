from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class SnippetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_titles = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'created_by', 'tags', 'tag_titles']
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        tag_titles = validated_data.pop('tag_titles', [])
        snippet = Snippet.objects.create(**validated_data)
        
        # Create or get tags
        for title in tag_titles:
            tag, _ = Tag.objects.get_or_create(title=title)
            snippet.tags.add(tag)
        
        return snippet

    def update(self, instance, validated_data):
        tag_titles = validated_data.pop('tag_titles', None)
        if tag_titles is not None:
            instance.tags.clear()
            for title in tag_titles:
                tag, _ = Tag.objects.get_or_create(title=title)
                instance.tags.add(tag)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance 