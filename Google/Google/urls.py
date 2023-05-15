"""
URL configuration for Google project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from googleApp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('search/', SearchPage.as_view(), name="searchPage"),
    path('images/', SearchImages.as_view(), name="imagesPage"),
    path('videos/', SearchVideos.as_view(), name="videosPage"),
    path('chat/', ChatMessages.as_view(), name="chat"),
    path('chat/message/', Send_message.as_view(), name="send"),
    path('chat/clear', Delete_chat.as_view(), name="clear"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
