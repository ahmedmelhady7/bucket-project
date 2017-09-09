#!/usr/bin/env python
"""
Test case class for bucketlist model
"""
from django.test import TestCase
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
