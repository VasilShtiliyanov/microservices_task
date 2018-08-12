from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.conf import settings
from .models import Job
from .request_handler import handle_requests
from .serializer import JobSerializer


@api_view(['GET'])
def job_with_categories(request):
    job_title = request.GET.get('job_title')
    url = '{}{}'.format(settings.API_URL, request.method)
    if job_title is not None:
        param = {'job_title': job_title}
        response = handle_requests(method=request.method, url=url, params=param)
        for index in range(0, len(response)):
            response[index].update(param)
    else:
        response = handle_requests(method=request.method, url=url)
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_category_for_job_title(request):
    job_title = request.POST.get('job_title')
    category_name = request.POST.get('name')
    category_desc = request.POST.get('desc')
    url = '{}{}/'.format(settings.API_URL, request.method)
    existing_job = Job.objects.filter(title=job_title)

    data_for_category = {
        'name': category_name,
        'description': category_desc,
        'job_title': job_title
    }

    if existing_job.count() == 0:
        data_for_job = {'title': job_title}
        serializer = JobSerializer(data=data_for_job)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'message': serializer.error}, status=status.HTTP_400_BAD_REQUEST)

    handle_requests(method=request.method, url=url, params=data_for_category)

    return Response({'message': 'success'}, status=status.HTTP_200_OK)

