from rest_framework.serializers import (ModelSerializer, CharField,
                                        SerializerMethodField, DateTimeField)
from django.core.paginator import Paginator

from .models import Post, Comment


class PostSerializer(ModelSerializer):
    date = DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Post
        fields = ['title', 'slug', 'image', 'excerpt',
                  'date', 'comments_count']


class PopularPostSerializer(ModelSerializer):
    date = DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Post
        fields = ['title', 'slug', 'date', 'thumbnail']


class CommentSerializer(ModelSerializer):
    username = CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ['username', 'text']


class PostDetailsSerializer(ModelSerializer):
    date = DateTimeField(format="%d-%m-%Y %H:%M:%S")
    comments = SerializerMethodField('paginated_comments')

    class Meta:
        model = Post
        fields = ['title', 'slug', 'image',
                  'content', 'date', 'comments']

    pagination_data = {}

    def paginated_comments(self, obj):
        page_size = 10
        paginator = Paginator(obj.comments.all(), page_size)
        page = self.context['request'].query_params.get('page') or 1

        comments = paginator.get_page(page)
        self.pagination_data['total_pages'] = comments.paginator.num_pages
        self.pagination_data['next'] = comments.has_next()
        self.pagination_data['previous'] = comments.has_previous()
        serializer = CommentSerializer(comments, many=True)

        return serializer.data

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['pagination_data'] = self.pagination_data

        return response
