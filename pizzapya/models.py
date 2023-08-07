from django.db import models


class Topping(models.Model):
    """
    Toppings model. This model stores a topping that is used to build different types of pizzas.

    There are ten topping categories: Cheeses (default), Dessert, Fruits, Gourmet, Healthy, Herbs & Spices, Meats,
    Nuts & Seeds, Sauces, and Veggies.

    Images are uploaded to AWS S3 Bucket and the url is saved to the table.
    """
    name = models.CharField(max_length=100, unique=True)
    TOPPING_CATEGORIES = [
        ("cheeses", "Cheeses"),
        ("dessert", "Dessert"),
        ("fruits", "Fruits"),
        ("gourmet", "Gourmet"),
        ("healthy", "Healthy"),
        ("herbs_spices", "Herbs & Spices"),
        ("meats", "Meats"),
        ("nuts_seeds", "Nuts & Seeds"),
        ("sauces", "Sauces"),
        ("veggies", "Veggies"),
    ]
    category = models.CharField(
        max_length=30,
        choices=TOPPING_CATEGORIES,
        default="Cheeses",
    )
    img = models.ImageField(upload_to="img", max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    """
    Pizzas model. This model stores pizzas, prices, images, and their toppings.

    As different pizzas can share toppings, a many-top-many relationship is used.

    Images are uploaded to AWS S3 Bucket and the url is saved to the table.
    """
    name = models.CharField(max_length=100, unique=True)
    toppings = models.ManyToManyField(Topping, related_name="pizzas")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to="img", max_length=100)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name
