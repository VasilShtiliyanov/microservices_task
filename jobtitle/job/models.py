from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title