class CashDesk(object):
    money = {}

    def __init__(self):
        self.money = {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,
            1: 0
        }

    def take_money(self, diction):
        for key in diction:
            self.money[key] = diction[key]

    def total(self):
        total = 0
        for key in self.money:
            total += self.money[key] * key
        return total

my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
#print(my_cash_desk.total())


class Product(object):
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price

    def __str__(self):
        return "Name: {}".format(self.name)


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price,display_size, mega_pixels):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store(object):

    def __init__(self, name):
        self.name = name
        self.dict = {}
        self.count = 0

    def load_new_products(self, product, count):
        if product in self.dict:
            self.dict[product] += count
        else:
            self.dict[product] = count

    def list_products(self, product_class):

        for key in self.dict:
            if isinstance(key, product_class):
                print(str(key), self.dict[key])

    def sell_product(self, product):
        if product in self.dict and self.dict[product] > 0:
            self.count += product.profit()
            self.dict[product] -= 1
            return True
        else:
            return False

    def total_income(self):
        return self.count
