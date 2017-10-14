# -*- encoding: utf-8 -*-

from django.db import models


class Cmdlet(models.Model):
    '''
    PowerShell Cmdlet Model
    '''

    name = models.CharField(max_length=120, unique=True, db_index=True)
    verb = models.CharField(max_length=20, db_index=True, null=True)
    noun = models.CharField(max_length=100, db_index=True, null=True)
    module = models.CharField(max_length=80, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('noun',)


class CmdletParameter(models.Model):
    '''
    PowerShell Cmdlet Parameter Model
    '''

    name = models.CharField(max_length=120, db_index=True)
    parameter = models.CharField(max_length=240, db_index=True)
    parameter_type = models.CharField(max_length=1024, db_index=True)
    parameter_set = models.CharField(max_length=120, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class CmdletOutputType(models.Model):
    '''
    PowerShell Cmdlet Output Type Model
    '''

    name = models.CharField(max_length=120, db_index=True)
    output_type = models.CharField(max_length=1024, db_index=True, null=True)
