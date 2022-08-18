from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse

from django.core.cache import cache

from portfolio.models import PortfolioProject


class ContactViewTest(TestCase):
    def test_contact_page(self):
        response = self.client.get(reverse('contact'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/contact.html')

    def test_mail_is_sent(self):
        with self.settings(
            CACHES={
                'default': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                    'LOCATION': 'test-cache',
                }
            }
        ):
            with patch('portfolio.views.send_mail') as mocked_send_mail:
                response = self.client.post('/contact/', secure=True,
                                            data={'name': 'Name', 'email': 'asd@asd.asd', 'message': 'message'})
                self.assertTrue(mocked_send_mail.called)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(
                    response, 'portfolio/contact_success.html')

            cache.clear()


class RatelimiterTest(TestCase):
    def test_ratelimiter(self):
        with self.settings(
            CACHES={
                'default': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                    'LOCATION': 'test-cache',
                }
            }
        ):
            with patch('portfolio.views.send_mail'):
                for i in range(7):
                    response = self.client.post('/contact/', secure=True,
                                                data={'name': 'Name', 'email': 'asd@asd.asd', 'message': 'message'})
                self.assertEqual(response.status_code, 429)

            cache.clear()


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 projects for pagination tests
        number_of_projects = 10

        for i in range(number_of_projects):
            PortfolioProject.objects.create(
                title=f'Title {i}',
                slug=f'title-{i}',
                image='image.jpg',
                excerpt='excerpt-excerpt',
                content='content-content'
            )

    def test_correct_context(self):
        response = self.client.get(reverse('index-page'), secure=True)
        self.assertTrue(response.context['page'] == 'index')

    def test_index_page_uses_correct_template(self):
        response = self.client.get(reverse('index-page'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_pagination_is_six(self):
        response = self.client.get(reverse('index-page'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['all_projects']), 6)

    def test_lists_all_projects(self):
        # Get second page and confirm it has (exactly) remaining 4 items
        response = self.client.get(
            reverse('index-page')+'?page=2', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['all_projects']), 4)


class ProjectDetailsViewTest(TestCase):
    def setUp(self):
        self.portfolio_project_0 = PortfolioProject.objects.create(
            title='Title 1',
            slug='title-1',
            image='image.jpg',
            excerpt='excerpt-excerpt',
            content='content-content'
        )

    def tearDown(self):
        self.portfolio_project_0.delete()

    def test_project_details_uses_correct_template(self):
        response = self.client.get(
            reverse('project-details', kwargs={'slug': self.portfolio_project_0.slug}), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/project-details.html')

    def test_project_details_404(self):
        response = self.client.get(
            reverse('project-details', kwargs={'slug': 'slug'}), secure=True)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'portfolio/404.html')


class AboutViewTest(TestCase):
    def test_about_page_uses_correct_template(self):
        response = self.client.get(reverse('about'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/about.html')
