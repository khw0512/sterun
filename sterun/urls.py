from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path("admin/", admin.site.urls),
    path("", include("community.urls")),
    path("users/", include("users.urls")),
    path("rental/", include("rental.urls")),
    path("paypal/", include("paypal.urls")),
    path("events/", include("events.urls")),
    path("schedule/", include("scalendar.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)