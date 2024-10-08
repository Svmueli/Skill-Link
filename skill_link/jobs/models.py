from django.db import models
from django.contrib.auth.models import User

class JobPosting(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField()

    def __str__(self):
        return self.title

