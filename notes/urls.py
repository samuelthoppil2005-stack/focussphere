from django.urls import path
from . import views

urlpatterns = [

    path("", views.notes_view, name="notes"),

    path("add/", views.add_note, name="add_note"),
    
    path("view/<int:id>/", views.view_note, name="view_note"),

    path("edit/<int:id>/", views.edit_note, name="edit_note"),

    path("delete/<int:id>/", views.delete_note, name="delete_note"),

]