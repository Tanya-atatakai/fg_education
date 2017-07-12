from __future__ import unicode_literals

from django.conf.urls import url

from .views import PostDetailView, education_blog_post_list

urlpatterns = [
    url(r'^$', education_blog_post_list, name='education_blog_post_list'),
    url(r'^(?P<slug>.*)$', PostDetailView.as_view(),
        name="education_blog_post_detail"),
]
