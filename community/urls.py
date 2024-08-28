from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about_us, name="about_us"),
    path("cookie_policy/", views.cookie_policy, name="cookie_policy"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("terms_of_services/", views.terms_of_services, name="terms_of_services"),
    path("events/", views.events, name="events"),
    path("event_detail/<str:pk>", views.event_detail, name="event_detail"),
    path("rental/", views.rental_items, name="rental_items"),
    path("contact/", views.contact_us, name="contact_us"),
    path("mypage/search/", views.search, name="search"),
    path("check/",views.check, name="check"),
    path("mypage/<str:pk>", views.mypage, name="mypage"),
    path("data/", views.data, name="data"),
    path("event-table/", views.event_table, name="event_table"),
    path("inquiry/", views.inquiry, name="inquiry"),
    path("email/", views.email, name="email"),
]