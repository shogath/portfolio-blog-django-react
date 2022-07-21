from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.db.models import Count

from .models import Post, Comment
from .serializers import (PostSerializer, PostDetailsSerializer,
                          PopularPostSerializer)

# Create your views here.


class BlogPostPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class AllBlogPostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = BlogPostPagination


class PopularBlogPostsView(ListAPIView):
    queryset = Post.objects.all().annotate(
        num_comments=Count('comments')).order_by('-num_comments')[:4]
    serializer_class = PopularPostSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_blog_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostDetailsSerializer(
        post, context={'request': request}, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request):
    try:
        post = Post.objects.get(slug=request.data['post'])
    except Post.DoesNotExist:
        return Response({"detail": "Something went wrong, please try again."}, status=status.HTTP_400_BAD_REQUEST)

    comment = Comment()
    comment.user = request.user
    comment.text = request.data['text']
    comment.post = post
    comment.save()

    return Response('asdasd')
