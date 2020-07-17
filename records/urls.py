from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('record/new/', views.CreateRecord, name='record-create'),
    path('update/<str:pk>/', views.UpdateRecord, name='update-record'),
]
