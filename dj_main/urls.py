from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import ekzarta.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ekzarta.views.home, name='main'),
    path('training/',ekzarta.views.training, name='training'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
