class Electro:
    volt = 220

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_avialable = True

    def sell(self, budget_object):
        self.report()
        if self.is_avialable:
            self.is_avialable = False
            budget_object.money += self.price

    def report(self):
        if self.is_avialable:
            avail_text = "Да"
        else:
            avail_text = "Нет"
        print(f"""
|-----------------------------------------------|
|Наименование:      {self.brand} - {self.model} 
|Цена:              {self.price}                
|Есть в наличии:    {avail_text}                
|-----------------------------------------------|
    """)

class Budget:
    money = 0


comp_1 = Electro("HP", "Aspire", 700)
printer_1 = Electro("EPSON", "k2000", 300)
budget_wednesday = Budget()
print(budget_wednesday.money)  # txt, Database
comp_1.sell(budget_wednesday)
print(budget_wednesday.money)
printer_1.sell(budget_wednesday)
print(budget_wednesday.money)
printer_1.sell(budget_wednesday)
print(budget_wednesday.money)
