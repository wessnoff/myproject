from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ekzarta.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='main'),
    path('services/', services, name='services'),
    path('training/', training, name='training'),
    path('team/',team, name='team'),
    path('about/', about, name='about'),
    path('new/', MainView.as_view(), name='new_main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
