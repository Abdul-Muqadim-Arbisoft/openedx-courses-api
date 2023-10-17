"""
URLs for courses_api.
"""
from django.urls import path
from .views import hello_template

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="courses_api/base.html")),
    path('hello_template/', hello_template, name='hello_template'),
]
