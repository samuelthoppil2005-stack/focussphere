from django.urls import path
from . import views

urlpatterns = [
   path("", views.assignments_view, name="assignments"),

    path("add/", views.add_assignment, name="add_assignment"),

    path("edit/<int:id>/", views.edit_assignment, name="edit_assignment"),

    path("delete/<int:id>/", views.delete_assignment, name="delete_assignment"),
]