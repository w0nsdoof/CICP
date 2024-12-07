from django.urls import path
from .views import ForgetPasswordView, CheckOTPView

urlpatterns = [
    path('forgot_password', ForgetPasswordView.as_view(), name='forgot-password'),
    path('check_otp', CheckOTPView.as_view(), name='check-otp'),
]
