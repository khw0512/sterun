from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("event_write/", views.event_write, name="event_write"),
    path("event_register/<str:pk>", views.event_register, name="event_register"),
]