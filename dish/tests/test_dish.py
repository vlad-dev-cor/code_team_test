import typing

from django.urls import reverse
from rest_framework.test import APITestCase

from dish.tests.factories import FoodCategoryFactory, FoodFactory


class ReportBuilderViewTestCase(APITestCase):

    def _get_category_with_published_food(self) -> typing.Any:
        return reverse(
            'dish_api:is_publish'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.food_category1 = None
        self.food_category2 = None
        self.food_category3 = None

        self.food1 = None
        self.food2 = None
        self.food3 = None
        self.food4 = None
        self.food5 = None

    def setUp(self) -> None:
        self.food_category1 = FoodCategoryFactory()
        self.food_category2 = FoodCategoryFactory()
        self.food_category3 = FoodCategoryFactory()

        self.food1 = FoodFactory(
            category=self.food_category1
        )
        self.food2 = FoodFactory(
            category=self.food_category1
        )
        self.food3 = FoodFactory(
            category=self.food_category1,
            is_publish=False
        )
        self.food4 = FoodFactory(
            category=self.food_category2,
            is_publish=False
        )
        self.food5 = FoodFactory(
            category=self.food_category2,
            is_publish=False
        )

    def test_get_category_with_published_food(self) -> None:
        change_campaign_data_url = self._get_category_with_published_food()
        response = self.client.get(change_campaign_data_url, format='json')
        self.assertEqual(response.status_code, 200)

        # Проверка на количество выводимых категорий, по условию одна (self.food_category1)
        self.assertEqual(len(response.data), 1)
