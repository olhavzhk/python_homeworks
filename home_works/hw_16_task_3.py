# guided by chatGPT
class Product:
    def __init__(self, prod_type, name, price):
        self.prod_type = prod_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product type.")
        elif amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        product.price *= 1.3
        for item in self.products:
            if item.name == product.name:
                item.amount += amount
                break
        else:
            product.amount = amount
            self.products.append(product)

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("The percent value should be between 0 and 100.")
        for product in self.products:
            if identifier_type == 'name' and product.name == identifier:
                product.price *= (1 - percent / 100)
            elif identifier_type == 'type' and product.type == identifier:
                product.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name:
                if product.amount >= amount:
                    product.amount -= amount
                    return
                else:
                    raise ValueError("Not enough amount of this product in the Store. ")
        else:
            raise ValueError("Product not found")

    def get_income(self):
        total_income = sum(product.price * product.amount for product in self.products)
        return total_income

    def get_all_products(self):
        return [(product.name, product.amount) for product in self.products]

    def get_product_info(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product_name, product.amount


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
