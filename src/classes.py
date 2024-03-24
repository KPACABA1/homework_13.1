class Category:
    """Класс имеет свойства: название, описание, товары(приватный). Так же атрибуты класса: общее количество категорий
    и общее количество уникальных продуктов"""
    total_number_of_categories = 1
    total_number_of_unique_products = 1

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.__products = products

    # Создал геттер для вывода списка продуктов
    @property
    def printing_products(self):
        for sequence in self.__products:
            print(f"{sequence['name']}, {sequence["price"]} руб. Остаток: {sequence["quantity"]}")

    # Создал сеттер для добавления нового продукта в список продуктов
    @printing_products.setter
    def printing_products(self, new_product):
        self.__products.append(new_product)


class Product:
    """Класс имеет свойства: название, описание, цена(приватный) и количество в наличии"""
    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    # Добавил класс-метод который позволяет создавать новые экземпляры класса
    @classmethod
    def new_product(cls, new_title, new_description, new_price, new_quantity_in_stock):
        return cls(new_title, new_description, new_price, new_quantity_in_stock)

    # Создаю геттер для вывода цены
    @property
    def printing_price(self):
        return self.__price

    # Создаю сеттер для вывода цены
    @printing_price.setter
    def printing_price(self, new_prise):
        """Если цена ниже или равно 0, то верну сообщение, если все нормально, то верну цену"""
        if new_prise > 0:
            self.__price = new_prise
        else:
            return "Цена введена некорректная"
