from rest_framework import serializers
from . import models


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'subject', 'email_body', 'created_at',)
        model = models.Email