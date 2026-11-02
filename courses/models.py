
from django.db import models

class CourseDb(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=50)
    course_fee = models.IntegerField()
    instructor = models.CharField(max_length=100)
    course_category = models.CharField(max_length=100)

