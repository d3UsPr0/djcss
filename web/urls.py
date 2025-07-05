from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('staff/', views.staff, name='staff'),
    path('welcome/', views.read_more, name='read_more'),
    path('bulletins/', views.bulletins, name='bulletins'),
    path('events/', views.events, name='events'),
    path('prayers/', views.prayers, name='prayers')

]

