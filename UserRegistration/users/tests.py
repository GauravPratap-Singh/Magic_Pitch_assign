from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        url = reverse('user-registration')
        data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('user_id' in response.data)

class UserDetailsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', email='test@example.com')
        self.user.set_password('testpassword')
        self.user.save()

    def test_user_details(self):
        url = reverse('user-details')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'test_user')

class ReferralsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='referrer', email='referrer@example.com')
        self.referred_user = User.objects.create(username='referred', email='referred@example.com', referral_code='referrer')

    def test_referrals(self):
        url = reverse('referrals')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['username'], 'referred')
