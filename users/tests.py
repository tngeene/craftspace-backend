from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


# test the user registration endpoint
class RegistrationTestCase(APITestCase):
    def test_artist_registration(self):
        data = {"email": "testartist@craftspace.com",
                "password": "PASwwordLit", 'first_name': 'Test', 'last_name': 'Artist', 'membership_type': 'Artist', 'phone_number': '0722880531'}
        response = self.client.post('/api/v1/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_trainer_registration(self):
        data = {"email": "testcollector@craftspace.com",
                "password": "PASwwordLit", 'membership_type': 'Collector', 'first_name': 'Test', 'last_name': 'Collector', 'phone_number': '0722880532'}
        response = self.client.post('/api/v1/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# test case for the userprofile model


class userProfileTestCase(APITestCase):
    def setUp(self):
        # create a new user making a post request to djoser endpoint
        self.user = self.client.post('/api/v1/auth/users/', data={
                                     'email': 'artist@test.com', 'password': 'testpassword123', 'first_name': 'Test', 'last_name': 'Artist', 'membership_type': 'Artist', 'phone_number': '0722880532'})
        # obtain an auth token for the newly created user
        response = self.client.post(
            '/api/v1/auth/token/login/', data={'email': 'artist@test.com', 'password': 'testpassword123'})
        self.token = response.data['auth_token']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token)

    def test_artist_profile_create(self):
        response = self.client.post(reverse('users:artists:artist_profile_list_create'), data={'user': User.objects.get(
            id=1), 'gender': 'male', 'bio': 'test bio', 'birth_place': 'Kitui', 'country': 'Kenya', 'county': 'Kitui'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_memberprofile_detail_retrieve(self):
        self.client.post(reverse('users:artists:artist_profile_rud'), data={
                         'user': User.objects.get(id=1), 'is_disabled': True, 'description': 'test desc'}, kwargs = {'pk': 1})
        response = self.client.get(
            reverse('users:artists:artist_profile_rud', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        profile_data = {'bio': 'I am a very famous artist',
                        'country': 'Tanzania', }
        response = self.client.patch(reverse(
            'users:artists:artist_profile_rud', kwargs={'pk': 1}), data=profile_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
