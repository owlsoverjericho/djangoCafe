from django.contrib import admin
from .models import DishCategory, Dish, Gellery, Forms

# Register your models here.

admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Gellery)
admin.site.register(Forms)