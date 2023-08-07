from django.shortcuts import render
from .models import Topping, Pizza


def index(request):
    """
    Main page where all pizzas and pizza toppings are displayed, as well as their images,
    prices, categories, and it is on sale. Could be used to expand into an
    ecommerce system in the future.
    """
    toppings = Topping.objects.order_by('name').all()
    pizzas = Pizza.objects.order_by('name').all()

    output = []
    for key, pizza in enumerate(pizzas):
        pizza_dict = {
            'id': pizzas[key].id,
            'name': pizzas[key].name,
            'price': pizzas[key].price,
            'img': pizzas[key].img,
            'on_sale': pizzas[key].on_sale,
            'toppings': ""
        }

        topping_list = pizzas[key].toppings.all()
        topping_count = len(topping_list)
        for t_key, topping in enumerate(topping_list):
            pizza_dict['toppings'] += f"{topping.name}"
            if t_key != topping_count - 1:
                pizza_dict['toppings'] += ", "

        output.append(pizza_dict)

    return render(request, "home.html", {'toppings': toppings, 'pizzas': output})


def pizza(request, id):
    """
    Detail page where a specific Pizza is displayed, its image,
    price, a list of all toppings that come on the pizza, and
    if it is on sale.
    """
    pizza = Pizza.objects.get(id=id)
    toppings = pizza.toppings.all()

    return render(request, "pizza.html", {'pizza': pizza, 'toppings': toppings})


def topping(request, id):
    """
    Detail page where a specific topping is displayed, its image,
    price, category, and a list of all pizzas that include the topping.
    """
    topping = Topping.objects.get(id=id)

    return render(request, "topping.html", {'topping': topping})

