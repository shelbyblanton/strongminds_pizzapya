# Generated by Django 4.2.4 on 2023-08-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzapya', '0002_remove_pizza_deleted_at_remove_pizza_last_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(related_name='pizzas', to='pizzapya.topping'),
        ),
    ]
