from django.urls import path

from .views import (
    user_login, two_factor_verify, toggle_two_factor, dashboard
)

app_name = 'authentication'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('2fa-verify/', two_factor_verify, name='2fa-verify'),
    path('toggle-two-factor/', toggle_two_factor, name='toggle_two_factor'),
    path('dashboard/', dashboard, name='dashboard'),
]