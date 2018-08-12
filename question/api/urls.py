from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    url(r'^GET/$',
        views.get_categories_from_job_title,
        name='category-detail'),
    url(r'^POST/$', views.create_category, name='create_category')
])
