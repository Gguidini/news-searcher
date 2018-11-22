"""news_searcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from interface import views
from news_searcher import settings

urlpatterns = [
    path('', views.index, name='url_index'),
    path('settings/', views.settings, name='url_settings'),
    path('results/', views.result, name='url_results'),
    path('output/', views.output, name='url_output')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # serve media files in development.