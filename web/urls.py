from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('staff/', views.staff, name='staff'),
    path('welcome/', views.read_more, name='read_more'),
    path('bulletins/', views.bulletins, name='bulletins'),
    path('events/', views.events, name='events'),
    path('prayers/', views.prayers, name='prayers'),
    path('videos/', views.videos, name='videos'),
    path('contact-us/', views.contact, name='contact-us'),
    path('admissions/', views.admissions, name='admissions'),
    path('academics/', views.academics, name='academics'),
    path('gallery/', views.gallery, name='gallery'),
    path('downloads/', views.publication_list, name='downloads'),
    path('publications/<int:pk>/increment_download/', views.increment_download_count, name='increment_download'),

]

