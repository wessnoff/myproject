from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from ekzarta.views import (MainView)
from ekzarta.views import (home, services, training, team, about)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='main'),
                  path('services/', services, name='services'),
                  path('training/', training, name='training'),
                  path('team/', team, name='team'),
                  path('about/', about, name='about'),
                  path('new/', MainView.as_view(), name='new_main'),
                  path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
                       name='robots'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
