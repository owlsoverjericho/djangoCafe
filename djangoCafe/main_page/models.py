from django.db import models
from django.core.validators import RegexValidator
from uuid import uuid4
from os import path

# Create your models here.

class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f'{self.name}: {self.position}'
    class Meta:
        ordering = ["position"]

class Dish(models.Model):
    def get_file_mame(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)


    def __str__(self) -> str:
        return f'{self.name}: {self.position}'
    
    class Meta:
            ordering = ["position"]

    name = models.CharField(max_length=50, unique=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE) #category is a foreign key from DishCategory class/table
    is_special = models.BooleanField(default=False)
    desc = models.TextField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingridients = models.CharField(max_length=100, blank=False)
    photo = models.ImageField(upload_to=get_file_mame)

class Gallery(models.Model):
    def get_file_mame(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/gallery', filename)
    
    photo = models.ImageField(upload_to=get_file_mame)
    desc = models.CharField(max_length=100, blank=False)
    is_visible = models.BooleanField(default=True)

class UserReservationFormModel(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message="The entered phone number seems to be incorrect")
    #email_validator = RegexValidator(regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', message="The entered email address number seems to be incorrect")

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    persons = models.SmallIntegerField()
    message = models.TextField(max_length=200)
    #email = models.EmailField(max_length=50, validators=[email_validator])
    #reservation_date = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
    order_processed_date = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-date"]
    
    def __str__(self) -> str:
        return f'{self.name} {self.phone}: {self.message[:20]}'
    
class ContactFormModel(models.Model):
    email_validator = RegexValidator(regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', message="The entered email address number seems to be incorrect")
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, validators=[email_validator])
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    order_processed_date = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-date"]
    
    def __str__(self) -> str:
        return f'{self.name} {self.phone}: {self.message[:20]}'