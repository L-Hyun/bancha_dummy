import json
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from core.utils import loginDecorator
from .models import Item
from .serializers import ItemSerializer

class AddItem(APIView):
  def post(self, req):
    data = json.objects.loads(req.body.decode('utf-8'))
    item = Item.create_item(
      title = data['title'],
      categroy = data['category'],
      seller = data['seller'],
      price = data['price'],
      discountedPrice = data['dPrice'],
      hashtags = data['hashtags'],
      thumb = data['thumb'],
      detail = data['detail']
    )
    return Response(status=200)

class getItem(APIView):
  def get(self, itemnumber):
    target = Item.objects.get(item_id=itemnumber)
    if (target is not None):
      return Response(ItemSerializer(target).data)
    else:
      return Response(status=404)
