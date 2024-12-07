import random,datetime

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .security import create_token, decrypt_token
from .serializers import ForgotPasswordSerializer, CheckOTPSerializer


class ForgetPasswordView(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    def post(self, request, *args, **kwargs):
        serilaizer = self.serializer_class(data=request.data)
        serilaizer.is_valid(raise_exception=True)

        email = serilaizer.validated_data['email']
        user = get_object_or_404(User, email=email)
        otp = str(random.randint(100000, 999999))
        print(otp) # TODO: dont leave it
        payload = {
            'user_id': user.id,
            'email': user.email,
            'otp': otp,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=10)
        }
        token = create_token(payload)

        send_mail(
            'OTP for Forget Password',
            f'Your Otp is {otp}',
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        
        return Response({ 'token': token }, status=200)
        
class CheckOTPView(GenericAPIView):
    serializer_class = CheckOTPSerializer
    def post(self, request, *args, **kwargs):
        serialzier = self.serializer_class(data=request.data)
        serialzier.is_valid(raise_exception=True)

        otp = serialzier.validated_data['otp']
        enc_token = serialzier.validated_data['token']

        data = decrypt_token(enc_token)
        if data['status']:
            otp_real = data['payload']['otp']
            if otp == otp_real:
                email = data['payload']['email']
                user = User.objects.get(email=email)
                access_token = str(RefreshToken.for_user(user).access_token)

                return Response(
                    {
                        'access_token': access_token,
                        'status': True,
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'OTP didnt matched....'
                }, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({
                'message': 'OTP expired...Try Again!!',
                'status': False
            }, status=status.HTTP_400_BAD_REQUEST)