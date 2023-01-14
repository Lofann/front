from django.db import models
import datetime
# Create your models here.

#Можно сделать один класс и наследовать есть, но сейчас вообще не до этого

class Home(models.Model):
    title = models.CharField('title', max_length=100, default='homepage')
    text = models.TextField('text', default=None)
    image = models.ImageField('img', default=None, upload_to='home')

    def __str__(self):
        return self.title

class Demand(models.Model):
    title = models.CharField('title', max_length=100, default='demand')
    text = models.TextField('text', default=None)
    graph_first = models.ImageField('graph_first', default=None, upload_to='demand')
    graph_second = models.ImageField('graph_second', default=None, upload_to='demand')

    def __str__(self):
        return self.title

class Geography(models.Model):
    title = models.CharField('title',max_length=100, default='geography')
    text = models.TextField('text', default=None)
    table = models.TextField('table', default=None)
    graph = models.ImageField('graph', default=None, upload_to='geography')

    def __str__(self):
        return self.title

class Skills(models.Model):
    title = models.CharField('title', max_length=100, default='skills')
    text = models.TextField('text', default=None)
    graph = models.ImageField('graph', default=None, upload_to='skills')

    def __str__(self):
        return self.title

