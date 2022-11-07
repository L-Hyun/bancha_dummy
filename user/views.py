import json
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from core.utils import loginDecorator
from .models import User
from .serializers import UserSerializer

class Register(APIView):
  def post(self, request):
    data = json.loads(request.body.decode('utf-8'))
    user = User.objects.create_user(
      email = data["email"],
      nickname = data['nickname'],
      password = data['password']
    )
    token = Token.objects.create(user=user)
    return Response({"Token": token.key})

class Login(APIView):
  def post(self, request):
    data = json.loads(request.body)
    user = auth.authenticate(username=data["email"], password=data["password"])
    if (user is not None):
      token = Token.objects.get(user=user)
      if (token is None):
        token = Token.objects.create(user=user)
      return Response({"Token": token.key})
    else:
      return Response(status=401)

class Logout(APIView):
  @loginDecorator
  def get(self, request):
    user = request.user
    token = Token.objects.get(user=user)
    token.delete()
    return Response({"Logout"})

class ChangePassword(APIView):
  @loginDecorator
  def post(self, request):
    data = json.loads(request.body)
    newPassword = data["newPassword"]
    user = request.user
    user.set_password(newPassword)
    user.save()
    
    #Change Token
    token = Token.objects.get(user=user)
    token.delete()
    token = Token.objects.create(user=user)
    return Response({"Token": token.key})

class GetUser(APIView):
  def get(self, req):
    return Response(UserSerializer(req.user).data)

class chk(APIView):
  def get(self, req):
    return Response(UserSerializer(User.objects.all(), many=True).data)

class getToken(APIView):
  def get(self, req, usernumber):
    token = Token.objects.get(user = User.objects.get(user_id=usernumber))
    return Response({"Token": token.key})

class getU(APIView):
  def get(self, req, usernumber):
    print(User.objects.get(user_id=usernumber))
    print(type(User.objects.get(user_id=usernumber)))
    return Response(UserSerializer(User.objects.get(user_id = usernumber)).data)

class verifyEmail(APIView):
  def post(self, request):
    data = json.loads(request.body)
    try:
      user = User.objects.get(email=data['email'])
      return Response({"isValid": False})
    except:
      return Response({"isValid": True})

class verifyNickname(APIView):
  def post(self, request):
    data = json.loads(request.body)
    try:
      user = User.objects.get(nickname=data['nickname'])
      return Response({"isValid": False})
    except:
      return Response({"isValid": True})
