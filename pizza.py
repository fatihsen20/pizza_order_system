"""
Bu dosyada pizza sınıfı oluşturulur.
Bu sınıf abstract bir sınıftır ve diğer sınıfların üst sınıfıdır.
"""
class Pizza:
    def get_cost(self):
        """
        Bu fonksiyon pizza sınıfının cost değişkenini döndürür.
        """
        return self.__class__.cost
    
    def get_description(self):
        """
        Bu fonksiyon pizza sınıfının description değişkenini döndürür.
        Description değişkeni bu sınıftan türetilen alt sınıfların isimlerini temsil eder.
        """
        return self.__class__.__name__