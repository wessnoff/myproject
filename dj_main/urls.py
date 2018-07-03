from django.contrib import admin
from django.urls import path
import ekzarta.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ekzarta.views.home, name='home'),
]
