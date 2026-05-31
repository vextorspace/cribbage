from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('news/', views.news_index, name='news_index'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('events/', views.events, name='events'),
    path('photographs/', views.photographic_register, name='photographic_register'),
    path('photographs/tribunal-exhibits/', views.tribunal_exhibits, name='tribunal_exhibits'),
    path('membership/apply/', views.membership_apply, name='membership_apply'),
    path('scoring/calculator/', views.scoring_calculator, name='scoring_calculator'),
    path('contact/', views.contact, name='contact'),
]
