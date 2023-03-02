# Generated by Django 4.1.5 on 2023-03-02 11:32

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_dish_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gellery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=main_page.models.Gellery.get_file_mame)),
                ('desc', models.CharField(max_length=100)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ['position']},
        ),
    ]