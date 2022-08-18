from django.urls import reverse
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from jwt_auth.models import User
from blog.models import Post


class AllBlogPostsViewTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.posts_url = reverse('posts')

        # Create 5 posts for pagination tests
        number_of_posts = 5

        for i in range(number_of_posts):
            Post.objects.create(
                title=f'Title {i}',
                slug=f'title-{i}',
                image='image.jpg',
                excerpt='excerpt-excerpt',
                content='content-content'
            )

    def test_all_blog_posts_get(self):
        response = self.client.get(self.posts_url, secure=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pagination_is_three(self):
        response = self.client.get(self.posts_url, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 5)
        self.assertEqual(len(response.data['results']), 3)

    def test_lists_all_posts(self):
        # Get second page and confirm it has (exactly) remaining 2 items
        response = self.client.get(self.posts_url + '?page=2', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 5)
        self.assertEqual(len(response.data['results']), 2)


class PopularBlogPostsViewTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.posts_url = reverse('popular_posts')

        # Create 5 posts for tests
        number_of_posts = 5

        for i in range(number_of_posts):
            Post.objects.create(
                title=f'Title {i}',
                slug=f'title-{i}',
                image='image.jpg',
                excerpt='excerpt-excerpt',
                content='content-content'
            )

    def test_popular_blog_posts_get(self):
        response = self.client.get(self.posts_url, secure=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_four_popular_posts(self):
        response = self.client.get(self.posts_url, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)


class BlogPostsDetailsViewTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()

        Post.objects.create(
            title=f'Title 1',
            slug=f'title-1',
            image='image.jpg',
            excerpt='excerpt-excerpt',
            content='content-content'
        )

    def test_blog_post_doesnt_exist(self):
        response = self.client.get(reverse('post_details',
                                           kwargs={'slug': 'title-10'}), secure=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_blog_post_exists(self):
        response = self.client.get(reverse('post_details',
                                           kwargs={'slug': 'title-1'}), secure=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Title 1')


class AddCommentViewTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.add_comment_url = reverse('add_comment')
        cls.user = User.objects.create(
            username='user1',
            email='asd@asd.asd',
            password=make_password('test_Pass1'),
        )

        Post.objects.create(
            title=f'Title 1',
            slug=f'title-1',
            image='image.jpg',
            excerpt='excerpt-excerpt',
            content='content-content'
        )

    def test_add_comment_unauthenticated(self):
        comment_data = {
            'text': 'comment text',
            'post': 'title-1'
        }
        response = self.client.post(self.add_comment_url,
                                    data=comment_data,
                                    secure=True)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_comment_valid(self):
        comment_data = {
            'text': 'comment text',
            'post': 'title-1'
        }
        self.client.login(email='asd@asd.asd', password='test_Pass1')
        response = self.client.post(self.add_comment_url,
                                    data=comment_data,
                                    secure=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_comment_post_doesnt_exist(self):
        comment_data = {
            'text': 'comment text',
            'post': 'title-10'
        }
        self.client.login(email='asd@asd.asd', password='test_Pass1')
        response = self.client.post(self.add_comment_url,
                                    data=comment_data,
                                    secure=True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
