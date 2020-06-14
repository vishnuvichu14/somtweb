from django.shortcuts import render
from django.contrib.auth.models import User, AnonymousUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.forms import UserRegistrationForm
from web.models import Profile


class ApiLogin(APIView):
    def post(self, request):
        data = request.data
        email = data['email']
        password = data['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                token = Token.objects.get(user=user)
                # profile = Profile.objects.get(user=user)
                return Response({'user_id': user.id, 'email': user.email, 'status': 'success', 'token': token.key},
                                status=400)
            else:
                return Response({'status': 'error', 'message': 'Incorrect Password'}, status=400)
        except User.DoesNotExist:
            return Response({'status': 'error', 'message': 'User does not exist'}, status=400)

    def get(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response({'message': 'Incorrect Username/Password', 'status': 'error'}, status=400)
        else:
            user = request.user
            return Response(
                {'email': user.username, 'name': user.first_name, 'status': 'success'})


class ApiRegistration(APIView):
    def post(self, request):
        print("SignUp :", request.POST)
        user_registration_form = UserRegistrationForm(request.data, request=request)
        if user_registration_form.is_valid():
            token = user_registration_form.save()
            return Response(
                {'status': 'success', 'message': 'User registered successfully!', "token": token.key})
        else:
            return Response({'status': 'error', 'errors': user_registration_form.errors})
