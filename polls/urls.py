from django.urls import path
from . import views
from .views import home, index, polls

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('polls/', index, name='polls_index'),
    path('fetch-articles/', polls, name='fetch_polls'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.user_login, name='login'),
    path('vote/', views.vote, name='vote'),
    path('profile/', views.profile, name='profile'),
]
