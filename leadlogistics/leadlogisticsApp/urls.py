from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import REDIRECT_FIELD_NAME
from . import views

app_name = 'leadlogisticsApp'

urlpatterns = [
    #path('login/',auth_views.LoginView.as_view(),name = 'login'),
    #re_path(r'^detail/(?P<pk>\d+)/$', views.DocketDetail.as_view(), name= 'detail'),
    #path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name = 'login'),
    #path('docketstatus/',views.DocketCreate.as_view(), name = 'docketstatus'),
    path('nodata/',views.nodata, name = 'nodata'),
    path('list/',views.DocketList, name = 'list'),
    path('detail/',views.DetailList, name = 'detail'),
    path('ContactUs/',views.ContactUs, name = 'ContactUs'),

    #path('detail/<int:pk>/', views.DocketDetail.as_view(), name= 'detail'),
    #re_path(r'^detail/(?P<pk>\d+)/$', views.DocketDetail.as_view(), name= 'detail'),
    #path('detail/(?P<slug>[-\w]+)/',views.DocketDetail.as_view(), name = 'detail'),
    #path('detail/',views.DocketDetail.as_view(), name = 'detail'),
    #re_path(r'^(?P<pk>\d+)/$', views.DocketDetail.as_view(), name= 'detail'),

    #path('signup/',views.SignUp.as_view(),name = 'signup')

]
