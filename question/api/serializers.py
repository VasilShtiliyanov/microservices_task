from rest_framework import serializers
from .models import Category, Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('name', 'answer', 'sequence', 'rows')


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'description', 'job_title')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.job_title = validated_data.get('job_title', instance.job_title)
        instance.save()
        return instance

    def to_representation(self, obj):
        serialized_data = super(CategorySerializer, self).to_representation(obj)  # original serialized data
        category_name = serialized_data['name']
        questions = Question.objects.filter(category__name=category_name)
        serialized_questions = QuestionSerializer(questions, many=True)
        serialized_data['questions'] = serialized_questions.data
        return serialized_data  # return modified serialized data


