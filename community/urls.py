from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about_us, name="about_us"),
    path("events/", views.events, name="events"),
    path("event_detail/<str:pk>", views.event_detail, name="event_detail"),
    path("rental/", views.rental_items, name="rental_items"),
    path("contact/", views.contact_us, name="contact_us"),
    path("mypage/search/", views.search, name="search"),
    path("check/",views.check, name="check"),
    path("mypage/<str:pk>", views.mypage, name="mypage"),
    path("data/", views.data, name="data"),
    path("inquiry/", views.inquiry, name="inquiry"),
    path("email/", views.email, name="email"),
]