from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    # path('programs/', views.weekly_programs_view, name='weekly-programs'),
]

