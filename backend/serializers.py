# -*- encoding: utf-8 -*-

from rest_framework import serializers

from backend import models


class CmdletSerilaizer(serializers.ModelSerializer):
    '''
    Cmdlet Serializer
    '''

    verb = serializers.SerializerMethodField()
    noun = serializers.SerializerMethodField()

    def get_verb(self, obj):
        if not obj.verb:
            return obj.name.split('-')[0]

    def get_noun(self, obj):
        if not obj.noun:
            return obj.name.split('-')[0]

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
