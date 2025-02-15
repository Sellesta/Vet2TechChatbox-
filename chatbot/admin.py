from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Subject, Question, UserPerformance, EntranceExam, CourseCompletion

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(UserPerformance)
admin.site.register(EntranceExam)
admin.site.register(CourseCompletion)
