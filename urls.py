from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('play/', views.play, name='play'),
    path('logout/', views.logout_view, name='logout'),
    path('save-score/', views.save_score, name='save_score'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
