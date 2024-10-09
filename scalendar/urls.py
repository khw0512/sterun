from django.urls import path

from . import views

app_name = "schedule"

urlpatterns = [
    path("<str:id>/<str:user_id>", views.schedule, name="schedule"),
]