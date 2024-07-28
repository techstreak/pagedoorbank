from django.contrib import admin
from django.urls import path, include
from bank.views import show_links
urlpatterns = [
    path('', show_links, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('bank.urls')),
]
