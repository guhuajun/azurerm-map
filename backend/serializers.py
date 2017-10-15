# -*- encoding: utf-8 -*-

from rest_framework import serializers

from backend import models


class CmdletSerilaizer(serializers.ModelSerializer):
    '''
    Cmdlet Serializer
    '''

    class Meta:
        model = models.Cmdlet
        fields = '__all__'


class CmdletParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CmdletParameter
        fields = '__all__'


class CmdletOutputTypeSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = models.CmdletOutputType
        fields = '__all__'
