"""
views for edx_course.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import filters

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.course_api.serializers import CourseSerializer


class CourseListAPIView(ListAPIView):
    queryset = CourseOverview.get_all_courses().select_related(
        'image_set'
    )
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['display_name', 'language']
