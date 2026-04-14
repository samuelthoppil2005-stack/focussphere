from django.urls import path
from . import views

urlpatterns = [
    path('', views.ai_chat_page, name='ai_page'),
    path('chat/', views.ai_chat, name='ai_chat'),
]