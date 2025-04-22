from rest_framework import serializers
from .models import *
class MediaStudentSerializer(serializers.ModelSerializer):
    # size_readable = serializers.SerializerMethodField()  # Add readable size field

    class Meta:
        model = Media
        fields = [
            'id',
            'title',
            'file',
           
        ]
 
class MediaSerializer(serializers.ModelSerializer):
    size_readable = serializers.SerializerMethodField()  # Add readable size field

    class Meta:
        model = Media
        fields = [
            'id',
            'alternative_test',
            'title',
            'caption',
            'description',
            'file',
            'size',
            'size_readable',  # Include the readable size
            'url',
            'course',
        ]

    def get_size_readable(self, obj):
        """Converts size from bytes to a readable format."""
        size = obj.size
        if size is None:
            return "0 B"
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
class MediaVideoSerializer(serializers.ModelSerializer):
    size_readable = serializers.SerializerMethodField()  # Add readable size field

    class Meta:
        model = Media_video
        fields = [
            'id',
            'alternative_test',
            'title',
            'caption',
            'description',
            'file',
            'size',
            'size_readable',  # Include the readable size
            'url',
            'course',
        ]

    def get_size_readable(self, obj):
        """Converts size from bytes to a readable format."""
        size = obj.size
        if size is None:
            return "0 B"
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024

