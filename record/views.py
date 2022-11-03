import json
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models import Q

from core.utils import loginDecorator
from .models import Record
from .serializers import RecordSerializer

from item.models import Item
from item.serializers import ItemSerializer

class AddRecord(APIView):
  def post(self, reqest):
    data = json.loads(reqest.body.decode('utf-8'))
    record = Record.objects.create_review(
      ordered_date = data['ordered_date'],
      experience_date = data['experience_date'],
      linked_item = data['linked_item'],
      linked_user = data['linked_user'],
      orderer_name = data['orderer_name'],
      orderer_phone = data['orderer_phone'],
      orderer_email = data['orderer_email']
    )
    return Response(RecordSerializer(record).data)

class GetRecords(APIView):
  def get(self, req):
    response = list()
    recs = Record.objects.filter(Q(linked_user=req.user.nickname))
    for record in recs:
      temp = {}
      temp['record'] = RecordSerializer(record).data
      item = Item.objects.get(item_id=record.linked_item)
      temp['item'] = ItemSerializer(item).data
      response.append(temp)
    return Response(response)