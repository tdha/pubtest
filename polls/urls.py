from django.urls import path

from . import views
# from .views import home
# from .views import headlines_news
# from .views import fetch_articles

urlpatterns = [
    path("", views.home, name="home"),
    path("polls/", views.index, name="polls_index"),
]