from django.shortcuts import render, redirect
from .models import Dish, DishCategory, Gallery
from .forms import UserReservationForm
import random

# Create your views here.


def main_page(req):

    if req.method == "POST":
        reservation_form = UserReservationForm(req.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return redirect("/")

    # query everything from this table/class (e.g. it's instances)
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specials = Dish.objects.filter(is_visible=True, is_special=True)
    gallery = list(Gallery.objects.filter(is_visible=True))
    gallery = random.sample(gallery, 8)
    reservation_form = UserReservationForm()

    return render(req, 'main_page.html', context={
        "categories": categories,
        "dishes": dishes,
        "specials": specials,
        "gallery": gallery,
        "reservation_form": reservation_form,
        })
