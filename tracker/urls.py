from django.urls import path
from . import views

urlpatterns = [
    # The home page
    path('', views.index, name='index'),
    # The search page
    path('add/', views.add_show, name='add_show'),
    # The invisible link that marks episodes as watched
    path('api/mark_watched/', views.mark_watched, name='mark_watched'),
]
