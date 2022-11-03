import json
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models import Q

from core.utils import loginDecorator
from .models import Review
from .serializers import ReviewSerializer

class AddReview(APIView):
  def post(self, req):
    data = json.loads(req.body.decode('utf-8'))
    review = Review.objects.create_review(
      linked_item = data['linked_item'],
      linked_user = data['linked_user'],
      score = data['score'],
      text = data['text'],
      written_date = data['written_date']
    )
    return Response(ReviewSerializer(review).data)

class GetReviews(APIView):
  def get(self, req, itemnumber):
    reviews = Review.objects.filter(Q(linked_item=itemnumber))
    return Response(ReviewSerializer(reviews, many=True).data)
