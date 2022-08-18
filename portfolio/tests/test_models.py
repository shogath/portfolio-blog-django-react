import random
import string

from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models import PortfolioProject


class PortfolioProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.portfolio_project_0 = PortfolioProject.objects.create(
            title='Title 1',
            slug='title-1',
            image='image.jpg',
            excerpt='excerpt-excerpt',
            content='content-content'
        )

        cls.portfolio_project_1 = PortfolioProject.objects.create(
            title='Title 2',
            slug='title-2',
            image='image.jpg',
            excerpt='excerpt-excerpt',
            content='content-content'
        )

    def tearDown(self):
        self.portfolio_project_0.delete()
        self.portfolio_project_1.delete()

    def test_created_properly(self):
        self.assertEqual(self.portfolio_project_0.title, 'Title 1')
        self.assertEqual(self.portfolio_project_0.slug, 'title-1')
        self.assertEqual(self.portfolio_project_0.image, 'image.jpg')
        self.assertEqual(self.portfolio_project_0.excerpt, 'excerpt-excerpt')
        self.assertEqual(self.portfolio_project_0.content, 'content-content')

    def test_update_portfolio_project_title(self):
        self.portfolio_project_0.title = 'new title'
        self.portfolio_project_0.save()
        self.assertEqual(self.portfolio_project_0.title, 'new title')

    def test_update_portfolio_project_slug(self):
        self.portfolio_project_0.slug = 'new-title'
        self.portfolio_project_0.save()
        self.assertEqual(self.portfolio_project_0.slug, 'new-title')

    def test_update_portfolio_project_image(self):
        self.portfolio_project_0.image = 'img.png'
        self.portfolio_project_0.save()
        self.assertEqual(self.portfolio_project_0.image, 'img.png')

    def test_update_portfolio_project_excerpt(self):
        self.portfolio_project_0.excerpt = 'new excerpt'
        self.portfolio_project_0.save()
        self.assertEqual(self.portfolio_project_0.excerpt, 'new excerpt')

    def test_update_portfolio_project_content(self):
        self.portfolio_project_0.content = 'new content'
        self.portfolio_project_0.save()
        self.assertEqual(self.portfolio_project_0.content, 'new content')

    def test_validation_portfolio_project_title(self):
        self.portfolio_project_0.title = ''.join(
            random.choice(string.ascii_uppercase) for _ in range(151))
        try:
            self.portfolio_project_0.full_clean()
        except ValidationError as e:
            self.assertTrue('title' in e.message_dict)

    def test_validation_portfolio_project_slug(self):
        self.portfolio_project_0.slug = 'title-2'
        try:
            self.portfolio_project_0.full_clean()
        except ValidationError as e:
            self.assertTrue('slug' in e.message_dict)

    def test_validation_portfolio_project_excerpt(self):
        self.portfolio_project_0.excerpt = 'excerpt'
        try:
            self.portfolio_project_0.full_clean()
        except ValidationError as e:
            self.assertTrue('excerpt' in e.message_dict)

    def test_validation_portfolio_project_content(self):
        self.portfolio_project_0.content = 'con'
        try:
            self.portfolio_project_0.full_clean()
        except ValidationError as e:
            self.assertTrue('content' in e.message_dict)
