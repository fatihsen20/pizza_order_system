from pizza_types import Classic, Margherita, TurkishPizza, PlainPizza
from topping_types import Olive, Mushroom, GoatCheese, Meat, Onion, Corn

import csv
import datetime

def main():
    """
    Bu fonksiyon kullanıcıdan pizza tabanı ve ekstra malzemeleri seçmesini isteyerek
    pizza sınıfından türetilen sınıfların nesnelerini oluşturur.
    Bu nesneleri kullanarak pizza sınıfının get_cost ve get_description fonksiyonlarını çağırır.
    Ekrana pizza ismi ve fiyatı yazdırılır.
    Son olarak siparişi veren kullanıcı bilgileri kaydedilir.
    """
    with open("Menu.txt", "r", encoding="utf-8") as file:
        menu = file.read()
    
    class_dict = {1: Classic, 2: Margherita, 3: TurkishPizza, 4: PlainPizza, 
              11: Olive, 12: Mushroom, 13: GoatCheese, 14: Meat, 15: Onion, 16: Corn}

    print(menu)
    code = input("Pizza Tabanı Seçiniz: ")

    while code not in ["1", "2", "3", "4"]:
        code = input("Lütfen Geçerli Bir Pizza Tabanı Seçiniz (1-4 Arası): ")
    
    order = class_dict[int(code)]()
    
    toppings = []

    while True:
        code = input("Ekstra Malzeme Seçiniz(Çıkmak İçin 0'a Basın): ")
        if code == "0":
            break

        elif code in toppings:
            print("Bu Malzeme Zaten Eklenmiş. Lütfen Başka Bir Malzeme Seçiniz.")
            continue

        while code not in ["11", "12", "13", "14", "15", "16"]:
            code = input("Lütfen Geçerli Bir Ekstra Malzeme Seçiniz (11-16 Arası): ")

            if code in toppings:
                print("Bu Malzeme Zaten Eklenmiş. Lütfen Başka Bir Malzeme Seçiniz.")
                continue

        order = class_dict[int(code)](order)
        toppings.append(code)
    
    print(f"{order.get_description()} : {order.get_cost()}£")

    name = input("Lütfen Adınızı Giriniz: ")
    ID = input("Lütfen TC Kimlik Numaranızı Giriniz: ")
    credit_card = input("Lütfen Kredi Kartı Numaranızı Giriniz: ")
    credit_card_pass = input("Lütfen Kredi Kartı Şifrenizi Giriniz: ")
    time_of_order = datetime.datetime.now()

    with open("Orders_Database.csv", "a") as orders:
        writer = csv.writer(orders, delimiter=",")
        writer.writerow([name, ID, credit_card, credit_card_pass, order.get_description(), time_of_order])
    
if __name__ == "__main__":
    main()