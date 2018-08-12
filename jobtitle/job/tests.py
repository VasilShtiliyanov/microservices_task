from django.test import TestCase
from .models import Job
# Create your tests here.


class JobTestCase(TestCase):
    def setUp(self):
        Job.objects.create(title="Python Dev")
        Job.objects.create(title="Django Dev")

    def test_jobs(self):
        python_dev = Job.objects.get(title="Python Dev")
        django_dev = Job.objects.get(title="Django Dev")

        self.assertEquals(python_dev.title, "Python Dev")
        self.assertEquals(django_dev.title, "Django Dev")
