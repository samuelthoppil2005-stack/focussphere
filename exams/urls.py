from django.urls import path
from . import views

urlpatterns = [

    path("", views.exams_view, name="exams"),

    path("add/", views.add_exam, name="add_exam"),
    
    path("edit/<int:id>/", views.edit_exam, name="edit_exam"),

    path("delete/<int:id>/", views.delete_exam, name="delete_exam"),

]