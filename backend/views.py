# -*- encoding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet

from backend import models, serializers


class CmdletViewSet(ModelViewSet):
    '''
    Cmdlet ViewSet
    '''

    queryset = models.Cmdlet.objects.all()
    serializer_class = serializers.CmdletSerilaizer


class CmdletParameterViewSet(ModelViewSet):
    '''
    Cmdlet Parameter ViewSet
    '''

    queryset = models.CmdletParameter.objects.all()
    serializer_class = serializers.CmdletParameterSerializer


class CmdletOutputTypeViewSet(ModelViewSet):
    '''
    Cmdlet OutputType ViewSet
    '''

    queryset = models.CmdletOutputType.objects.all()
    serializer_class = serializers.CmdletOutputTypeSerilaizer
