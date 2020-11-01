from django.urls import path
from . import views


app_name = 'search_main'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]