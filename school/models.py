from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    # students = models.ManyToManyField(Students)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.course_name


