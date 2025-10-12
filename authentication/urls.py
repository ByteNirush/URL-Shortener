from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns =[
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    # Confirmation page to show a GUI with a logout button
    path('logout/confirm/', TemplateView.as_view(template_name='logout_confirm.html'), name='logout_confirm'),
    # Logout via POST, then redirect to login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]