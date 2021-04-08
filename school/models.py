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


#mightve not worked

# class Courses(models.Model):
#     course_name = models.CharField(max_length=255)
#     students = models.ManyToManyField(
#         Students, 
#         through="Enrollments", 
#         through_fields=('course', 'student' )
#     )

#     def __str__(self):
#         return self.course_name

# # join table
# class Enrollments(models.Model):
#     course = models.ForeignKey(Courses, on_delete=models.CASCADE)
#     student = models.ForeignKey(Students, on_delete=models.CASCADE)