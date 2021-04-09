#DJANGO REST
from rest_framework import serializers
from .models import Student, Course

class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'courses']


class CourseSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'students'] # add students?



#MANUEL METHOD

# from builtins import object

# class StudentSerializer(object):
#     def __init__(self, body):
#         self.body = body

#     @property
#     def all_students(self):
#         output = {'students': []}

#         for each in self.body:
#             student_details = {
#                 'id': each.id,
#                 'first_name': each.first_name,
#                 'last_name': each.last_name,
#                 'age': each.age
#             }
#             output['students'].append(student_details)

#         return output
    
#     @property
#     def student_detail(self):
#         # breakpoint()
#         courses = []
#         # course.objects.filter()
#         for course in self.body.courses.all():
#             courses.append({'course_name': course.course_name})
#         return {
#             'id': self.body.id,
#             'first_name': self.body.first_name,
#             'last_name': self.body.last_name,
#             'age': self.body.age,
#             'courses': courses
#         }


# class CourseSerializer(object):
#     def __init__(self, body):
#         self.body = body
    
#     @property
#     def all_courses(self):
#         output = {'courses': []}
#         for each in self.body:
#             course_details = {
#                 'id': each.id,
#                 'course_name': each.course_name
#             }
#             output['courses'].append(course_details)

#         return output


#     @property
#     def course_detail(self):
#         students = []
#         for student in self.body.students.all():
#             students.append({
#                 'id': student.id,
#                 'first_name': student.first_name,
#                 'last_name': student.last_name,
#                 'age': student.age
#                 })
#         return {
#             'id': self.body.id,
#             'course_name': self.body.course_name,
#             'students': students
#         }