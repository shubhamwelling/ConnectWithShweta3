"""poll_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from poll import views as poll_views
from poll.views import suggestions
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructions/', poll_views.instructions, name='instructions'),
    path('how/', poll_views.how, name='how'),
    path('privacy/', poll_views.privacy, name='privacy'),
    path('date/<poll_id>/', poll_views.date, name='date'),
    path('suggestions/<poll_id>/', poll_views.suggestions, name='suggestions'),
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    ]
    #path('resultsdata/<str:obj>/', poll_views.resultsData, name = "resultsdata"),
