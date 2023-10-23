from django.urls import path
from courses_api.views import get_courses

urlpatterns = [
    path(
        'list/', get_courses, name='get_courses_list'
    )
]
