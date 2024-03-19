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
