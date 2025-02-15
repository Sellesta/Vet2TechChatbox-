from django.urls import path
from .views import chatbot_view  # Ensure this matches views.py

urlpatterns = [
    path('chat/', chatbot_view, name='chatbot'),
]
