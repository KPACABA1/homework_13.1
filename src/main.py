import json


class Category:
    """Класс имеет свойства: название, описание, товары. Так же атрибуты класса: общее количество категорий и общее
    количество уникальных продуктов"""
    title: str
    description: str
    products: list

    total_number_of_categories = 1
    total_number_of_unique_products = 1

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products


class Product:
    """Класс имеет свойства: название, описание, цена и количество в наличии"""
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


def reading_a_file():
    """Создаю функцию для возврата Paython списка из файла  для дальнейшего присвоения данных к классам"""
    with open("products.json", "rt", encoding='utf-8') as products_json:
        products_python = json.load(products_json)
        return products_python


# Присваиваю первой категории из файла "products.json"(смартфонам) класс Category
category_1 = Category(reading_a_file()[0]["name"], reading_a_file()[0]["description"], reading_a_file()[0]["products"])
# Присваиваю 3 товарам класс Product
product_1_1 = Product(reading_a_file()[0]["products"][0]["name"], reading_a_file()[0]["products"][0]["description"],
                      reading_a_file()[0]["products"][0]["price"], reading_a_file()[0]["products"][0]["quantity"])
product_1_2 = Product(reading_a_file()[0]["products"][1]["name"], reading_a_file()[0]["products"][1]["description"],
                      reading_a_file()[0]["products"][1]["price"], reading_a_file()[0]["products"][1]["quantity"])
product_1_3 = Product(reading_a_file()[0]["products"][2]["name"], reading_a_file()[0]["products"][2]["description"],
                      reading_a_file()[0]["products"][2]["price"], reading_a_file()[0]["products"][2]["quantity"])

# Присваиваю второй категории(Телевизоры) класс Category
category_2 = Category(reading_a_file()[1]["name"], reading_a_file()[1]["description"], reading_a_file()[1]["products"])
# Присваиваю 1 товару класс Product
product_2_1 = Product(reading_a_file()[1]["products"][0]["name"], reading_a_file()[1]["products"][0]["description"],
                      reading_a_file()[1]["products"][0]["price"], reading_a_file()[1]["products"][0]["quantity"])
