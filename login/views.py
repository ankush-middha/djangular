from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer, ProfileImageSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class RegistrationApi(APIView):
    '''
    TEST APP.
    API to register new User
    '''
    serializer_class = RegistrationSerializer

    def get_serializer_class(self):
        return self.serializer_class

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # create user object if serializer is valid
            user_obj = User.objects.create(**serializer.data)
            # set password to convert password into hash
            user_obj.set_password(serializer.data['password'])
            token_obj, created = Token.objects.get_or_create(user=user_obj)
            user_obj.save()
            return Response({'token': token_obj.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    '''
    Login APi - pass username and password to login
    return token and username
    '''
    serializer_class = LoginSerializer

    def get_serializer_class(self):
        return self.serializer_class

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                user_obj = User.objects.get(email=serializer.data['email'])
            except:
                return Response({'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            if user_obj.check_password(serializer.data['password']):
                token, created = Token.objects.get_or_create(user=user_obj)

                return Response({'token': token.key,
                                 'username': user_obj.username}, status=status.HTTP_200_OK)
            return Response({'username password not matched'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApi(APIView):
    '''
    API to get and update profile details
    '''
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.serializer_class

    def get(self, request):
        user = request.user
        user_serializer = self.serializer_class(user)#, context={'request':request})
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = User.objects.filter(id=request.user.id)
            if 'contact_no' in serializer.data:
                if User.objects.filter(contact_no=serializer.data['contact_no']).count():
                    return Response('This number is already registered with us!', status=status.HTTP_400_BAD_REQUEST)

            data_dict = serializer.data
            data_dict.pop("profile_pic")
            user.update(**data_dict)
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileImageApi(APIView):
    '''
    Api to get and update profile image
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileImageSerializer

    def get_serializer_class(self):
        return self.serializer_class

    def put(self, request):

        user_obj = User.objects.get(id=request.user.id)
        # import pdb;pdb.set_trace()
        serializer = self.serializer_class(user_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data= {}
            data['profile_pic'] = "http://" + request.META['HTTP_HOST'] + serializer.data['profile_pic']
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)