from django.db import models


# Create your models here.
class CameraNumbers(models.Model):
    Classroom = models.PositiveIntegerField()
    Cameras = models.PositiveIntegerField()

    def __str__(self):
        return 'Classroom'

    class Meta:
        verbose_name_plural = 'Camara Numbers'
