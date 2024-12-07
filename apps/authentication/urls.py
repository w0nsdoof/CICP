from django.urls import path
from .views import (
    LoginView, RegisterUserView,
    ForgetPasswordView, CheckOTPView,
    )

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('forgot_password', ForgetPasswordView.as_view(), name='forgot-password'),
    path('check_otp', CheckOTPView.as_view(), name='check-otp'),
]
