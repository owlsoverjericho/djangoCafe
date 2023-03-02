from django.shortcuts import render
from .models import Dish, DishCategory

# Create your views here.

def main_page(req):
    categories = DishCategory.objects.filter(is_visible=True) #query everything from this table/class (e.g. it's instances)
    dishes = Dish.objects.filter(is_visible=True)
    specials = Dish.objects.filter(is_visible=True, is_special=True)

    return render(req, 'main_page.html', context={'categories': categories, "dishes": dishes, "specials": specials})