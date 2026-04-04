from django.urls import path
from . import views

urlpatterns = [
    path('', views.stage1, name='stage1'),
    path('stage2/', views.stage2, name='stage2'),
    path('stage3/', views.stage3, name='stage3'),
    path('stage4/', views.stage4, name='stage4'),
]