from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page URL
    path('guide/', views.smart_farming_guide, name='smart_farming_guide'),  # Separate guide page
    path('recommendation/recommend/', views.recommend, name='recommend'),
]
