import json
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models import Q

from core.utils import loginDecorator
from .models import Item
from .serializers import ItemSerializer

class AddItem(APIView):
  def post(self, req):
    data = json.loads(req.body.decode('utf-8'))
    item = Item.objects.create_item(
      title = data['title'],
      category = data['category'],
      seller = data['seller'],
      price = data['price'],
      discountedPrice = data['discountedPrice'],
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

class GetItems(APIView):
  def get(self, req):
    return Response(ItemSerializer(Item.objects.all(), many=True).data)

class GetItemsWithSection(APIView):
  def get(self, req, sectionnumber):
    idx = sectionnumber*15
    return Response(ItemSerializer(Item.objects.all()[idx : idx + 15], many=True).data)

class GetItemsWithCategory(APIView):
  def get(self, req, categorynumber):
    if (categorynumber == 0):
      return Response(ItemSerializer(Item.objects.all(), many=True).data)
    return Response(ItemSerializer(Item.objects.filter(Q(category=categorynumber)), many=True).data)