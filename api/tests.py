#!/usr/bin/env python
"""
Test case class for bucketlist model
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Bucketlist
class ModelTestCase(TestCase):
    """
    This class defines the test suite for the bucketlist model.
    """
    def setUp(self):
        """
        define the test client and other variables
        """
        user = User.objects.create(username="nerd")
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name, owner=user)

    def test_create_bucketlist(self):
        """
        Test the bucketlist model can create a bucketlist.
        """
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertEqual(old_count+1, new_count)

class ViewTestCase(TestCase):
    """
    Test suite for api views
    """
    def setUp(self):
        user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucketlist_data = { 'name': 'Go to Ibiza', 'owner': user.id }
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
        )
    def test_api_create_bucketlist(self):
        """
        Test the api has bucket creation capability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_get_bucketlist(self):
        """
        Test the api can get a given bucketlist.
        """
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_update_bucketlist(self):
        """
        Test the api can update a given bucketlist.
        """
        bucketlist = Bucketlist.objects.get()
        new_bucketlist = {
            "name": "New bucketlist"
        }
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            new_bucketlist,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_delete_bucketlist(self):
        """
        Test the api can delete a given bucketlist.
        """
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format="json",
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)