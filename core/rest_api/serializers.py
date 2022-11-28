from rest_framework import serializers
from management.models import ManagementUser
from entry.models import EntryRequest

class EntryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryRequest
        fields = [
            'email'
        ]

class ManagementUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementUser
        fields = [
            'name',
            'username',
            'birth_date',
            'national_code',
            'email',
            'salary',
        ]