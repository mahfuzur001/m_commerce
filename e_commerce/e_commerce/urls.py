from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import * 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index1, name="index1"),  # main homepage
    path("products/", include("products.urls")),  # ✅ আলাদা path prefix দাও
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
