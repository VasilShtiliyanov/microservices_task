from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    url(r'job/', views.job_with_categories),
    url(r'post/', views.create_category_for_job_title),
])