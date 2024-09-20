class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

    def __repr__(self):
        return self.__str__()


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        products = []
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    name, weight, category = line.strip().split(', ')
                    products.append(Product(name, float(weight), category))
        except FileNotFoundError:
            pass  # Если файл не найден, возвращаем пустой список
        return products

    def add(self, *products):
        products_list = self.get_products()
        with open(self.__file_name, 'a') as file:
            for prod in products:
                exists = any(p.name == prod.name for p in products_list)
                if exists:
                    print(f"Продукт {prod.name} уже есть в магазине")
                else:
                    file.write(f"{prod}\n")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
