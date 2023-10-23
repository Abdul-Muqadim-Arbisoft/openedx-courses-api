"""
URLs for edx_course.
"""
from django.urls import path

from courses_api.views import CourseListAPIView

urlpatterns = [
    path('list/', CourseListAPIView.as_view(), name='course_list'),
]
