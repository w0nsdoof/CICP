from django.urls import path

from .views import (
    register_view,login_view, logout_view, 
    two_factor_verify, toggle_two_factor, 
    dashboard
)

app_name = 'authentication'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('2fa-verify/', two_factor_verify, name='2fa-verify'),
    path('toggle-two-factor/', toggle_two_factor, name='toggle_2fa'),
    path('dashboard/', dashboard, name='dashboard'),
]