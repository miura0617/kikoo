from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.PostLisView.as_view(), name='index'),
]

