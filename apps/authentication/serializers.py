from rest_framework import serializers

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    
class CheckOTPSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)
    token = serializers.CharField()