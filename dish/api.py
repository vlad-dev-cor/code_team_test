
from django.db.models import Prefetch, Count, Q
from drf_yasg.utils import swagger_auto_schema, no_body
from requests import Response
from rest_framework.response import Response
from rest_framework.views import APIView

from dish.models import FoodCategory, Food
from dish.serializers.dish import FoodListSerializer


class IsPublishViewSet(APIView):

    @swagger_auto_schema(
        responses={
            200: FoodListSerializer()
        },
        request_body=no_body
    )
    def get(self, request):
        categories = FoodCategory.objects.annotate(
            food_count=Count('food',  filter=Q(food__is_publish=True)),
           )\
            .filter(food_count__gt=0) \
            .prefetch_related(Prefetch("food", queryset=Food.objects.filter(is_publish=True)))

        serializer = FoodListSerializer(categories, many=True)
        data = serializer.data
        return Response(data=data, content_type='application/json')
