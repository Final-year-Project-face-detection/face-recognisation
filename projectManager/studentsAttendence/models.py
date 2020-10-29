from django.db import models


# Create your models here.
class CameraNumbers(models.Model):
    SEMESTER = (
        ('1', 'First Semester'),
        ('2', 'Second Semester'),
        ('3', 'Third Semester'),
        ('4', 'Fourth Semester'),
        ('5', 'Fifth Semester'),
        ('6', 'Sixth Semester'),
        ('7', 'Seventh Semester'),
        ('8', 'Eighth Semester'),
    )
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
    YEAR = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    )
    SECTION = (
        ('A', 'A Section'),
        ('B', 'B Section'),
        ('C', 'C Section'),
    )
    Classroom = models.PositiveIntegerField()
    Cameras = models.PositiveIntegerField()
    semester = models.CharField(max_length=1, choices=SEMESTER, blank=True)
    branch = models.CharField(max_length=10, choices=BRANCHES, blank=True)
    year = models.CharField(max_length=1, choices=YEAR, blank=True)
    section = models.CharField(max_length=1, choices=SECTION, blank=True)


    def __str__(self):
        return 'Classroom'

    class Meta:
        verbose_name_plural = 'Camara Details'
