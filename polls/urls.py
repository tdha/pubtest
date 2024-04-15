from django.urls import path
from .views import home, index, fetch_articles

urlpatterns = [
    path('', home, name='home'),
    path('polls/', index, name='polls_index'),
    path('fetch-articles/', fetch_articles, name='fetch_articles'),
]

