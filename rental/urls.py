from django.urls import path
from . import views

app_name = "rental"

urlpatterns = [
    path("rental_register/", views.rental_register, name="rental_register"),
    path("update/<str:pk>", views.update, name="update"),
    path("delpage/<str:pk>", views.delpage, name="delpage"),
    path("delreserv/<str:pk>", views.delreserv, name="delreserv"),
]