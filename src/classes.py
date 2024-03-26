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

    @property
    def printing_products(self):
        """Создал геттер для вывода списка продуктов"""
        for sequence in self.__products:
            print(f"{sequence['name']}, {sequence["price"]} руб. Остаток: {sequence["quantity"]}")

    @printing_products.setter
    def printing_products(self, new_product):
        """Создал сеттер для добавления нового продукта в список продуктов"""
        self.__products.append(new_product)

    def __str__(self):
        """Вывожу данные в формате 'Название категории, количество продуктов: 200 шт.'"""
        # Считаю сколько товаров в категории
        quantity = 0
        for i in self.__products:
            quantity += i["quantity"]
        return f"{self.title}, количество продуктов:{quantity} шт."


class Product:
    """Класс имеет свойства: название, описание, цена(приватный) и количество в наличии"""
    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def new_product(cls, new_title, new_description, new_price, new_quantity_in_stock):
        """Добавил класс-метод который позволяет создавать новые экземпляры класса, а так же перед этим проверяет
        наличие нового экземпляра класса ранее, в случае обнаружения такого экземпляра, к нему добавляется количество
        товара старого экземпляра. У нового экземпляра выставляется максимальная цена среди 2 экземпляров"""
        # Реализую проверку наличия такого же товара
        # проверяю есть ли новый товар среди "Смартфонов" из файла json
        for i in range(len(reading_a_file()[0]["products"])):
            if new_title in reading_a_file()[0]["products"][i].values():
                # Если такой товар уже есть, то добавляю к нему количество старого товара
                new_quantity_in_stock += reading_a_file()[0]["products"][i]["quantity"]
                # Выставляю максимальную цену за товар
                highest_prise = max(reading_a_file()[0]["products"][i]["prise"], new_price)
                return cls(new_title, new_description, highest_prise, new_quantity_in_stock)

        # проверяю есть ли новый товар среди "Телевизоров" из файла json
        for i in range(len(reading_a_file()[1]["products"])):
            if new_title in reading_a_file()[1]["products"][i].values():
                # Если такой товар уже есть, то добавляю к нему количество старого товара
                new_quantity_in_stock += reading_a_file()[1]["products"][i]["quantity"]
                # Выставляю максимальную цену за товар
                highest_prise = max(reading_a_file()[1]["products"][i]["prise"], new_price)
                return cls(new_title, new_description, highest_prise, new_quantity_in_stock)

            # Если товар новый, то просто создаю новый экземпляр класса
            else:
                return cls(new_title, new_description, new_price, new_quantity_in_stock)

    @property
    def printing_price(self):
        """Создаю геттер для вывода цены"""
        return self.__price

    @printing_price.setter
    def printing_price(self, new_prise):
        """Создаю сеттер для вывода цены. Если цена ниже или равно 0, то верну сообщение, если все нормально, то проверю
         понижение цены"""
        if new_prise < 0:
            print("Цена введена некорректная")
        else:
            # Если старая цена больше новой, то запрошу подтверждение понижения цены
            if self.__price > new_prise:
                print("Подтвердите понижение стоимости написав 'Y' или 'N', если цену понижать не надо" )
                confirmation = input()
                if confirmation.lower() == "y":
                    self.__price = new_prise
                elif confirmation.lower() == "n":
                    return self.__price
            else:
                self.__price = new_prise

    def __str__(self):
        """Вывожу информацию в формате 'Название продукта, 80 руб. Остаток: 15 шт.'"""
        return f"{self.title}, {self.__price} руб. Остаток:{self.quantity_in_stock} шт."

    def __add__(self, other):
        """Складываю объекты между собой таким образом, чтобы результат выполнения сложения двух продуктов был сложением
         сумм, умноженных на количество на складе."""
        return self.__price * self.quantity_in_stock + other.__price * other.quantity_in_stock
