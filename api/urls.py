from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('num_to_english', views.num_to_english, name='convert'),
    path('num_to_english1', views.num_to_words, name='convert1'),
]
