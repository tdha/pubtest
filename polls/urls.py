from django.urls import path
from .views import home, index, polls

urlpatterns = [
    path('', home, name='home'),
    path('polls/', index, name='polls_index'),
    path('fetch-articles/', polls, name='fetch_polls'),
]
