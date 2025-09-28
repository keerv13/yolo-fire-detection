from django.contrib import admin
from django.urls import path
from detector.views import upload_image

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", upload_image, name="upload"),
]
