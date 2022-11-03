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
    data = json.loads(req.body.decode('utf-8'))
    item = Item.objects.create_item(
      title = data['title'],
      categroy = data['category'],
      seller = data['seller'],
      price = data['price'],
      discountedPrice = data['dPrice'],
      hashtags = data['hashtags'],
      thumb = data['thumb'],
      detail = data['detail']
    )
    return Response(ItemSerializer(item).data)

class GetItem(APIView):
  def get(self, req, itemnumber):
    target = Item.objects.get(item_id=itemnumber)
    if (target is not None):
      return Response(ItemSerializer(target).data)
    else:
      return Response(status=404)
