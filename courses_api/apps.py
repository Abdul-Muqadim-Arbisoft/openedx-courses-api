"""
courses_api Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType


class CoursesApiConfig(AppConfig):
    """
    Configuration for the courses_api Django application.
    """

    name = 'courses_api'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'courses_api',
                PluginURLs.APP_NAME: 'courses_api',
                PluginURLs.REGEX: r'^api/test/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
    }


"""
courses_api Django application initialization.
"""
#
#from django.apps import AppConfig
#
#
# class CoursesApiConfig(AppConfig):
#     """
#     Configuration for the courses_api Django application.
#     """
#
#     name = 'courses_api'
