# -*- encoding: utf-8 -*-
# pylint: disable=W0613

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
    search_fields = ('^component')

    @list_route()
    def verb(self, *args):
        '''Return verb list'''

        data = [x.verb for x in self.queryset.all()]
        data = sorted(list(set(data)))
        return Response(data=data)

    @list_route()
    def noun(self, *args):
        '''Return noun list'''
        data = [x.noun for x in self.queryset.all()]
        data = sorted(list(set(data)))
        return Response(data=data)

    @list_route()
    def component(self, *args):
        '''Return component list'''
        keyword = self.request.GET.get('search', None)
        alphabets = [chr(x) for x in range(97, 113)]
        data = [x.component for x in self.queryset.all()]
        if keyword in alphabets:
            data = [x.component for x in self.queryset.all()
                    if x.component.startswith(keyword.upper())]
        data = sorted(list(set(data)))
        return Response(data=data)

    @list_route()
    def noun_tree(self, *args):
        '''Return noun tree'''
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
    filter_fields = ('name', 'parameter', 'parameter_type')

    @list_route()
    def parameter(self, *args):
        '''Return parameter list'''
        data = [x.parameter for x in self.queryset.all()]
        data = sorted(list(set(data)))
        return Response(data=data)

    @list_route()
    def parametertype(self, *args):
        '''Return parameter type list'''
        data = [x.parameter_type for x in self.queryset.all()]
        data = sorted(list(set(data)))
        return Response(data=data)


class CmdletOutputTypeViewSet(ModelViewSet):
    '''
    Cmdlet OutputType ViewSet
    '''

    queryset = models.CmdletOutputType.objects.all()
    serializer_class = serializers.CmdletOutputTypeSerilaizer
    filter_fields = ('name', 'output_type')

    @list_route()
    def outputtype(self, *args):
        data = [x.output_type for x in self.queryset.all()]
        data = sorted(list(set(data)))
        return Response(data=data)
