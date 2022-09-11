from django.contrib import admin
from django.db.models import JSONField

from dish.models import Food, FoodCategory
from dish.widget import JSONEditorWidget


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'updated_at', 'created_at', 'category', 'is_vegan', 'is_special', 'code', 'internal_code',
        'name_ru', 'description_ru', 'description_en', 'description_ch', 'cost', 'is_publish'
    )

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    search_fields = ['id', 'name_ru']


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'updated_at', 'created_at', 'name_ru', 'name_en', 'name_ch', 'order_id'
    )

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    search_fields = ['id', 'name_ru', 'name_en']
