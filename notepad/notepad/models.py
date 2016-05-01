# -*- encoding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField('Título',max_length=32)
    content = models.TextField('Contenido')
    date = models.DateTimeField('Fecha', auto_now_add=True)
    user = models.ForeignKey(User)
    user.verbose_name = 'Usuario'
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = 'Nota'
    