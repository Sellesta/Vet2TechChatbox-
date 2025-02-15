from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)
    difficulty = models.IntegerField()

    def __str__(self):
        return self.question_text

class UserPerformance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_attempts = models.IntegerField(default=0)
    correct_attempts = models.IntegerField(default=0)

    def accuracy(self):
        return self.correct_attempts / self.total_attempts if self.total_attempts > 0 else 0

class EntranceExam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class CourseCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)

