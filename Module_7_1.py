class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"наименование: {self.name}, вес: {self.weight}, категория: {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()

    def add(self, *products):
        existing_products = self.get_products()
        for product in products:
            product_str = str(product)
            product_name = product.name
            if product_name not in existing_products:
                file = open(self.__file_name, 'a')
                file.write(product_str + '\n')
                file.close()
            else:
                print(f"Продукт {product_name} уже есть в магазине")


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')


s1.add(p1, p2, p3)

print(s1.get_products())