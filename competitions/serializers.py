from datetime import datetime

from rest_framework import serializers
from .models import competitions, bids, sellers, buyers


class competitionSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Validate JSON
        """
        if data['open'] > data['closed']:
            raise serializers.ValidationError("Competition open must be before closed")
        else:
            return data

    class Meta:
        model = competitions
        fields = '__all__'


class bidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bids
        fields = '__all__'


class sellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = sellers
        fields = '__all__'


class buyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = buyers
        fields = '__all__'
