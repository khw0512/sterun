from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("event_write/", views.event_write, name="event_write"),
    path("event_register/<str:pk>", views.event_register, name="event_register"),
    path("update_event/<str:pk>", views.update_event, name="update_event"),
    path("deleventpage/<str:pk>", views.deleventpage, name="deleventpage"),
    path("delevent/<str:pk>", views.delevent, name="delevent"),
    path("eventinfo", views.eventInfo, name="eventInfo"),
]