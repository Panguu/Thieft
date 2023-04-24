from django.test import TestCase

from .models import User, UserManager

class UserTestCase(TestCase):
    
    def setUp(self):
        """test for user object"""
        User.objects.create(username='testuser1', password='12345', token='example_token!')
        User.objects.create(username='testuser2', password='54321', token="right_token!")


    def testPassword(self):
        """test for user password"""
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')

        self.assertEqual(user1.password, '12345')
        self.assertEqual(user2.password, '54321')

    
    def testToken(self):
        """test for user token"""
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')

        self.assertEqual(user1.token, 'example_token!')
        self.assertNotEqual(user2.token, 'wrong_token!')
