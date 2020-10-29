from django.db import models


# Create your models here.
class FirstYear(models.Model):
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
    usn = models.CharField(max_length=10)
    branch = models.CharField(max_length=10, choices=BRANCHES)
    section = models.CharField(max_length=1, choices=SECTION)
    images = models.FileField(max_length=50, upload_to='FirstYear')

    class Meta:
        verbose_name_plural = 'First Year'


class SecondYear(models.Model):
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
    usn = models.CharField(max_length=10)
    branch = models.CharField(max_length=10, choices=BRANCHES)
    section = models.CharField(max_length=1, choices=SECTION)
    images = models.FileField(max_length=50, upload_to='SecondYear')

    class Meta:
        verbose_name_plural = 'Second Year'


class ThirdYear(models.Model):
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
    usn = models.CharField(max_length=10)
    branch = models.CharField(max_length=10, choices=BRANCHES)
    section = models.CharField(max_length=1, choices=SECTION)
    images = models.FileField(max_length=50, upload_to='ThirdYear')

    class Meta:
        verbose_name_plural = 'Third Year'


class FourthYear(models.Model):
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
    usn = models.CharField(max_length=10)
    branch = models.CharField(max_length=10, choices=BRANCHES)
    section = models.CharField(max_length=1, choices=SECTION)
    images = models.FileField(max_length=50, upload_to='FourthYear')

    class Meta:
        verbose_name_plural = 'Fourth Year'
