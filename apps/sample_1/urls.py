from django.conf.urls import url

from .views import json_to_html

urlpatterns = [
    url('^api', json_to_html),
]
