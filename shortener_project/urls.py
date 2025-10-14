from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create/', views.create_short_url, name='create'),
    path('delete/<int:id>/', views.delete_short_url, name='delete'),
    path('api/clicks/', views.clicks_snapshot, name='clicks_snapshot'),
    path('<str:code>/', views.redirect_short_url, name='redirect'),
]
