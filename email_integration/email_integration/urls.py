from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('emails.urls')),  # Подключение API маршрутов из приложения emails
    path('', include('emails.urls')),      # Подключение страниц из приложения emails
]
