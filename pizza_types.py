from pizza import Pizza

"""
Bu dosyada pizza sınıfından türetilen sınıflar oluşturulur.
Bu sınıflar pizza türlerini temsil eder.
Hepsinin cost değişkeni vardır ve pizza türlerinin fiyatlarını tutar.
Hepsinin description değişkeni vardır ve pizza türlerinin içeriklerini tutar.
"""

class Classic(Pizza):
    cost = 10
    def __init__(self):
        self.description = "Domates Sosu, Mozarella Peyniri ve Zeytinyağı"

class Margherita(Pizza):
    cost = 12
    def __init__(self):
        self.description = "Domates Sosu, Mozarella Peyniri, Zeytinyağı ve Fesleğen"

class TurkishPizza(Pizza):
    cost = 15
    def __init__(self):
        self.description = "Domates Sosu, Mozarella Peyniri, Sucuk, Zeytinyağı, Mantar ve Yeşil Biber"

class PlainPizza(Pizza):
    cost = 9
    def __init__(self):
        self.description = "Domates Sosu, Mozarella Peyniri"