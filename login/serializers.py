import urllib2
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("User with this email already exists.")
        else:
            return value

class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True)  # create to override model field ie to prevent save() call on post method
    class Meta:
        model = User
        fields =('email', 'password')


class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    class Meta:
        model = User
        fields= ('email', 'contact_no', 'username', 'profile_pic', 'gender')

    # def get_profile_pic(self, obj):
    #     try:
    #         if obj.fb_user_id and (obj.profile_pic.url.rfind('http') != -1):
    #             return urllib2.unquote(obj.profile_pic.url.replace('/media/', '').encode('utf8'))
    #         return "http://" + self.context['request'].META['HTTP_HOST'] + obj.profile_pic.url
    #     except:
    #         return ''


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('profile_pic',)