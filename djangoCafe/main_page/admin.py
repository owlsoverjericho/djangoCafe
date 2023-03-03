from django.contrib import admin
from .models import DishCategory, Dish, Gallery, UserReservationFormModel

# Register your models here.

admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Gallery)
admin.site.register(UserReservationFormModel)