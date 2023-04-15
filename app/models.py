from django.db import models
from rest_framework.reverse import reverse


NULLABLE = {'blank': True, 'null': True}


class EducationModule(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(**NULLABLE)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return self.name
