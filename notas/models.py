from django.db import models

class Nota(models.Model):
    title = models.CharField('Title', max_length=250)
    content = models.TextField('Content')
