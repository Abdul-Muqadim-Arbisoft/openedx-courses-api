"""
views for edx_course.
"""
from django.shortcuts import render


def hello_template(request):
    """
    Test working functionality.
    """
    return render(request, 'courses_api/hello.html')
