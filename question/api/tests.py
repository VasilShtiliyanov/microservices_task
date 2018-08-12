from django.test import TestCase
from .models import Question, Category

# Create your tests here.


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="MVC", description="Questions on MVC pattern", job_title="Python Dev")
        Question.objects.create(name="What is MVC", category=Category.objects.get(name="MVC"), rows=1, answer="You tell me...", sequence=1)

    def test_categories_and_questions(self):
        category = Category.objects.get(name="MVC")
        question = Question.objects.get(name="What is MVC")

        self.assertEquals(category.questions[0], question)
        self.assertEquals(category.description, "Questions on MVC pattern")
        self.assertEquals(question.answer, "You tell me...")
