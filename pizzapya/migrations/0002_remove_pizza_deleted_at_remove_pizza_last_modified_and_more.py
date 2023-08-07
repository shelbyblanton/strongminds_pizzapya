# Generated by Django 4.2.4 on 2023-08-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzapya', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='topping',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='topping',
            name='last_modified',
        ),
        migrations.AlterField(
            model_name='topping',
            name='category',
            field=models.CharField(choices=[('Cheeses', 'Cheeses'), ('Dessert', 'Dessert'), ('Fruits', 'Fruits'), ('Gourmet', 'Gourmet'), ('Healthy', 'Healthy'), ('Herbs & Spices', 'Herbs & Spices'), ('Meats', 'Meats'), ('Nuts & Seeds', 'Nuts & Seeds'), ('Sauces', 'Sauces'), ('Veggies', 'Veggies')], default='Cheeses', max_length=30),
        ),
    ]