#!/usr/bin/env python
"""
Test case class for bucketlist model
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Bucketlist
class ModelTestCase(TestCase):
    """
    This class defines the test suite for the bucketlist model.
    """
    def setUp(self):
        """
        define the test client and other variables
        """
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

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
        self.client = APIClient()
        self.bucketlist_data = { 'name': 'Go to Ibiza' }
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