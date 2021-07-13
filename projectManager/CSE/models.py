from django.db import models
from django.db.models.fields import DateTimeField


class FourthYearASec(models.Model):
    BRANCHES = (
        ('CSE', 'Computer Science Engineering'),
        ('ISE', 'Information Science Engineering'),
        ('ECE', 'Electronic Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CVE', 'Civil Engineering'),
        ('AI & ML', 'Artificial Intelligence and Machine Learning.'),
        ('TCE', 'Telecommunications Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
    )
    SECTION = (
        ('A', 'A Section'),
        ('B', 'B Section'),
        ('C', 'C Section'),
    )
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Fourth Year A Section'
