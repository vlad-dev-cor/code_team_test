import string

import factory
from factory import fuzzy

from dish.models import Food, FoodCategory


class FoodCategoryFactory(factory.django.DjangoModelFactory):
    name_ru = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    name_en = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    name_ch = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    order_id = factory.Faker('pyint', min_value=0, max_value=100)

    class Meta:
        model = FoodCategory


class FoodFactory(factory.django.DjangoModelFactory):
    category = None
    is_vegan = True
    is_special = True
    code = factory.Faker('pyint', min_value=0, max_value=1000)
    internal_code = factory.Faker('pyint', min_value=0, max_value=1000)
    name_ru = fuzzy.FuzzyText(length=4, chars=string.ascii_letters, prefix='')
    description_ru = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    description_en = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    description_ch = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    cost = factory.Faker('pyint', min_value=0, max_value=1000)
    is_publish = True

    class Meta:
        model = Food
