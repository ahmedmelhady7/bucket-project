#!/usr/bin/env python
"""
API model serializers
"""
from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Model instance into JSON format.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
