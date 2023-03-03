from pizza import Pizza

"""
Bu dosyada pizza ile ekstra malzemelerin birleştiği sınıf oluşturulur.
Bu sınıf pizza sınıfından türetilir.
"""
class PizzaDecorator(Pizza):

    def __init__(self, topping):
        """
        topping değişkeni ekstra malzemeyi temsil eder.
        """
        self.component = topping
    
    def get_cost(self):
        """
        Bu fonksiyon pizza ücretiyle ekstra malzeme ücretini toplamını döndürür.
        """
        return self.component.get_cost() +\
            Pizza.get_cost(self)
    
    def get_description(self):
        """
        Bu fonksiyon pizza ismiyle ekstra malzeme ismini birleştirerek döndürür.
        """
        return self.component.get_description() + " " + ", " +\
            Pizza.get_description(self)