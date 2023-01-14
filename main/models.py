import datetime

from django.db import models


# Create your models here




class Home(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='homepage')
    text = models.TextField('Текст', default=None)
    image = models.ImageField(
        'img', default=None,
        upload_to='home'
    )


class Demand(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='demand'
    )
    text = models.TextField('Текст', default=None)
    graph_left = models.ImageField(
        'График №2',
        default=None,
        upload_to='demand'
    )
    graph_right = models.ImageField(
        'График №1',
        default=None,
        upload_to='demand'
    )


class Geography(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geography'
    )
    text = models.TextField('Заголовок', default=None)
    table = models.TextField('Таблица', default=None)
    graph = models.ImageField(
        'График',
        default=None,
        upload_to='geography'
    )

class Skills(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    text = models.TextField('Текст', default=None)
