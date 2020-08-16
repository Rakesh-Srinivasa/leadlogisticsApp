"""leadlogistics URL Configuration

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
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MainView.as_view(),name = 'index'),
    path('fleet/',views.FleetView.as_view(),name = 'fleet'),
    #path('contact/',views.ContactView.as_view(),name = 'contact'),
    path('sample/',views.SampleView.as_view(),name = 'sample'),
    path('services/',views.ServiceView.as_view(),name = 'services'),
    path('Thanks/',views.Thanks.as_view(),name = 'Thanks'),
    path('leadlogisticsApp/',include('leadlogisticsApp.urls',namespace = 'leadlogisticsApp')),

]
