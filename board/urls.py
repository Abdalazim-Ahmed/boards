from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('board/<int:board_id>/', views.topic , name='topic'),
    path('board/<int:board_id>/new/', views.new_topic , name='new_topic'),

]
