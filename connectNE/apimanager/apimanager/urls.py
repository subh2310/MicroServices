from django.contrib import admin
from django.urls import path
from apimanager.views import ConnectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/connectNE/', ConnectView.as_view()),
]
