from django.urls import reverse
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from jwt_auth.models import User


class UserSignUpViewTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.signup_url = reverse('register_user')

    def test_if_data_is_correct_then_signup(self):
        signup_dict = {
            'username': 'user1',
            'email': 'asd@asd.asd',
            'password': 'test_Pass1',
            'password2': 'test_Pass1',
        }

        response = self.client.post(self.signup_url, signup_dict, secure=True)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

        new_user = User.objects.get(email='asd@asd.asd')
        self.assertEqual(new_user.username, 'user1')

    def test_if_username_already_exists_dont_signup(self):
        user = User()
        user.username = 'user1'
        user.email = 'asd@asd.asd'
        user.password = make_password('test_Pass1')
        user.save()

        signup_dict = {
            'username': 'user1',
            'email': 'asd@asd.asd',
            'password': 'test_Pass1',
            'password2': 'test_Pass1',
        }

        response = self.client.post(self.signup_url, signup_dict, secure=True)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['email'][0],
            "User with email 'asd@asd.asd' already exists."
        )

        # Check that there is only one user with the saved username
        username_query = User.objects.filter(email='asd@asd.asd')
        self.assertEqual(username_query.count(), 1)


class ObtainTokenPairViewTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            username='user1',
            email='asd@asd.asd',
            password=make_password('test_Pass1'),
        )
        cls.client = APIClient()
        cls.token_obtain_url = reverse('token_obtain_pair')

    def test_token_obtain_pair(self):
        login_dict = {
            'email': 'asd@asd.asd',
            'password': 'test_Pass1',
        }
        response = self.client.post(self.token_obtain_url,
                                    login_dict,
                                    secure=True)

        self.assertIn('access', response.data.keys())
        self.assertIn('refresh', response.data.keys())

    def test_token_obtain_pair_account_doesnt_exist(self):
        login_dict = {
            'email': 'zxc@zxc.zxc',
            'password': 'test_Pass1',
        }
        response = self.client.post(self.token_obtain_url,
                                    login_dict, secure=True)

        self.assertEqual(response.data['detail'],
                         'Incorrect email or password.')
