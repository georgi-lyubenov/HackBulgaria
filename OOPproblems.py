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


class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def print_fraction(self):
        return (str(self.num) + '/' + str(self.denom))


def add(Fraction1, Fraction2):
    return str(Fraction2.denom * Fraction1.num + Fraction2.num * Fraction1.denom) + '/' + str(Fraction1.denom * Fraction2.denom)


def subtract(Fraction1, Fraction2):
    return str(Fraction2.denom * Fraction1.num - Fraction2.num * Fraction1.denom) + '/' + str(Fraction1.denom * Fraction2.denom)


def equal(Fraction1, Fraction2):
    def simplify(Fraction3):
        def find_gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x
        result = Fraction(0, 0)
        result.num = Fraction3.num / find_gcd(Fraction3.num, Fraction3.denom)
        result.denom = Fraction3.denom / find_gcd(Fraction3.num, Fraction3.denom)
        return result
    if (simplify(Fraction1)).num == (simplify(Fraction2)).num and (simplify(Fraction1)).denom == (simplify(Fraction2)).denom:
        return True
    else:
        return False


def gt_or_lt(Fraction1, Fraction2):
    def find_gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x

    def simplify(Fraction3):
        result = Fraction(0, 0)
        result.num = Fraction3.num / find_gcd(Fraction3.num, Fraction3.denom)
        result.denom = Fraction3.denom / find_gcd(Fraction3.num, Fraction3.denom)
        return result
    if (simplify(Fraction1)).denom == (simplify(Fraction2)).denom:
        if (simplify(Fraction1)).num > (simplify(Fraction2)).num:
            print(Fraction1.print_fraction() + " is greater than " + Fraction2.print_fraction())
        else:
            print(Fraction1.print_fraction() + " is less than " + Fraction2.print_fraction())
    else:
        def lcm(x, y):
            return x * y // find_gcd(x, y)
        if Fraction1.num * (lcm(Fraction1.denom, Fraction2.denom) / Fraction1.denom) > Fraction2.num * (lcm(Fraction1.denom, Fraction2.denom) / Fraction2.denom):
            print(Fraction1.print_fraction() + " is greater than " + Fraction2.print_fraction())
        else:
            print(Fraction1.print_fraction() + " is less than " + Fraction2.print_fraction())


class Employee(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class HourlyEmployee(Employee):
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.per_hour = 100

    def weeklyPay(self, hours):
        if hours > 40:
            return self.hours * 1.5 * self.per_hour
        else:
            return self.hours * self.per_hour


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def weeklyPay(self, hours):
        return hours * (self.salary / 40)


class Manager(SalariedEmployee):

    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def weeklyPay(self, hours):
        return (self.salary / 40) * hours + (self.bonus / 40) * hours


