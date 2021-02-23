from rest_framework import serializers
from postings.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        # read_only_fields = ['title']
        # converts to json
        # validation for data passed
