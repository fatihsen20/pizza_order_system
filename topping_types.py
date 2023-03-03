from pizza_decorator import PizzaDecorator

"""
Bu dosyada ekstra malzemelerin sınıfları oluşturulur.
Bu sınıflar PizzaDecorator sınıfından türetilir.
Hepsinin cost değişkeni vardır ve ekstra malzemelerin fiyatlarını tutar.
"""
class Olive(PizzaDecorator):
    cost = 0.25
    def __init__(self, topping):
        PizzaDecorator.__init__(self, topping)

class Mushroom(PizzaDecorator):
    cost = 0.35
    def __init__(self, topping):
        PizzaDecorator.__init__(self, topping)
    
class GoatCheese(PizzaDecorator):
    cost = 0.50
    def __init__(self, topping):
        PizzaDecorator.__init__(self, topping)

class Meat(PizzaDecorator):
    cost = 0.75
    def __init__(self, topping):
        PizzaDecorator.__init__(self, topping)

class Onion(PizzaDecorator):
    cost = 0.25
    def __init__(self, topping):
        PizzaDecorator.__init__(self, topping)

class Corn(PizzaDecorator):
    cost = 0.25
    def __init__(self, topping):
        PizzaDecorator.__init__(self, topping)