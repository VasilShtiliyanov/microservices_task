from rest_framework import status

from .serializers import CategorySerializer, QuestionSerializer
from .models import Category, Question
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def get_categories_from_job_title(request):
    job_title = request.GET.get('job_title')
    if job_title is not None:
        categories = Category.objects.filter(job_title=job_title)
        serializer = CategorySerializer(categories, many=True)
    else:
        categories = Category.objects.filter()
        serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_category(request):
    category_name = request.POST.get('name')
    category_desc = request.POST.get('description')
    job_title = request.POST.get('job_title')

    data = {
        'name': category_name,
        'description': category_desc,
        'job_title': job_title
    }

    try:
        existing_category = Category.objects.get(name=category_name)
        serializer = CategorySerializer(existing_category, data=data)
    except Category.DoesNotExist:
        serializer = CategorySerializer(data=data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'message': serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'success'}, status=status.HTTP_200_OK)
