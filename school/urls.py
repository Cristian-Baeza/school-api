#DJANGO REST 

from django.urls import path, include
from .views import StudentViewSet, CourseViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course') #seems to work 
urlpatterns = router.urls




# MANUAL METHOD

# from django.urls import path
# from . import views

# #
# urlpatterns = [

#     #STUDENT URLS
#     path('students', views.student_list, name='student_list'),
#     path('students/new', views.new_student, name='new_student'),
#     path('students/<int:student_id>', views.student_detail, name='student_detail'),
#     path('students/<int:student_id>/edit', views.edit_student, name='edit_student'),
#     path('students/<int:student_id>/delete', views.delete_student, name='delete_student'),
    
#     #COURSES URLS
#     path('courses', views.course_list, name='course_list'),
#     path('courses/<int:course_id>', views.course_detail, name='course_detail'),
#     path('courses/new', views.new_course, name='new_course'),
#     path('courses/<int:course_id>/edit', views.edit_course, name='edit_course'),
#     path('courses/<int:course_id>/delete', views.delete_course, name='delete_course'),

#     # #NESTED URLS
#     path('courses/<int:course_id>/enroll/<int:student_id>', views.enroll_student, name='enroll_student'),   
#     path('courses/<int:course_id>/students/<int:student_id>/drop', views.drop_student, name='drop_student'),   
# ]