from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("status/", views.status, name="status"),
]
