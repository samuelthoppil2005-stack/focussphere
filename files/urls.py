from django.urls import path
from . import views

urlpatterns = [

    path("", views.files_view, name="files"),

    path("upload/", views.upload_file, name="upload_file"),

    path("delete/<int:id>/", views.delete_file, name="delete_file"),

]