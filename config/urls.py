from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("drcare.urls")),
    # path("", include("hello_world.urls")),
    # path('',include('my_blog.urls')),
    # path("",include("Barer_shop.urls")),
    path("",include("models.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

