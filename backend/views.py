# -*- encoding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import list_route

from backend import models, serializers


class CmdletViewSet(ModelViewSet):
    '''
    Cmdlet ViewSet
    '''

    queryset = models.Cmdlet.objects.all()
    serializer_class = serializers.CmdletSerilaizer
    filter_fields = ('name', 'verb', 'noun')

    @list_route()
    def verb(self, *args):
        data = [x.verb for x in self.queryset.all()]
        data = sorted(list(set(data)))
        return Response(data=data)

    @list_route()
    def noun(self, *args):
        data = [x.noun for x in self.queryset.all()]
        data = sorted(list(set(data)))
        return Response(data=data)
    
    @list_route()
    def noun_tree(self, *args):
        data = [x.noun for x in self.queryset.all()]
        data = sorted(list(set(data)))
        data = [{'exapand': True, 'title': x, 'children': []} for x in data]
        return Response(data=data)

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
