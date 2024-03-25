from functions import reading_a_file

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
        # Реализую проверку наличия такого же товара
        # проверяю есть ли новый товар среди "Смартфонов" из файла json
        for i in range(len(reading_a_file()[0]["products"])):
            if new_title in reading_a_file()[0]["products"][i].values():
                # Если такой товар уже есть, то добавляю к нему количество старого товара
                new_quantity_in_stock += reading_a_file()[0]["products"][i]["quantity"]
                # Если цена выше у старого товара, то меняю цену нового
                if reading_a_file()[0]["products"][i]["price"] > new_price:
                    highest_price = reading_a_file()[0]["products"][i]["price"]
                    return cls(new_title, new_description, highest_price, new_quantity_in_stock)
                # Если у нового товара цена выше, то цену не меняю
                else:
                    return cls(new_title, new_description, new_price, new_quantity_in_stock)
        # проверяю есть ли новый товар среди "Телевизоров" из файла json
        for i in range(len(reading_a_file()[1]["products"])):
            if new_title in reading_a_file()[1]["products"][i].values():
                # Если такой товар уже есть, то добавляю к нему количество старого товара
                new_quantity_in_stock += reading_a_file()[1]["products"][i]["quantity"]
                # Если цена выше у старого товара, то меняю цену нового
                if reading_a_file()[1]["products"][i]["price"] > new_price:
                    highest_price = reading_a_file()[1]["products"][i]["price"]
                    return cls(new_title, new_description, highest_price, new_quantity_in_stock)
                # Если у нового товара цена выше, то цену не меняю
                else:
                    return cls(new_title, new_description, new_price, new_quantity_in_stock)
            # Если товар новый, то просто создаю новый экземпляр класса
            else:
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
