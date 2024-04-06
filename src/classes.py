from src.functions import reading_a_file
from abc import ABC, abstractmethod


class AbstractCategory(ABC):
    """Создал абстрактный класс, просто для того, чтобы был"""
    @abstractmethod
    def __str__(self):
        """То же самое с методом, просто сделал его абстрактным, чтобы был"""
        pass


class Mixin:
    """Создал вывод в консоль о том, что был создан объект и его информацию"""
    def __init__(self, *args, **kwargs):
            print(self.__class__.__name__, *args, **kwargs)


class Category(Mixin, AbstractCategory):
    """Класс имеет свойства: название, описание, товары(приватный). Так же атрибуты класса: общее количество категорий
    и общее количество уникальных продуктов"""
    total_number_of_categories = 1
    total_number_of_unique_products = 1

    def __init__(self, title, description, products):
        super().__init__(title, description, products)
        self.title = title
        self.description = description
        self.__products = products

    @property
    def printing_products(self):
        """Создал геттер для вывода списка продуктов"""
        for sequence in self.__products:
            # Сначала я работал с файлом JSON, поэтому теперь я проверяю данные из файла или нет
            if isinstance(sequence, Product):
                print(sequence)
            else:
                print(f"{sequence['name']}, {sequence["price"]} руб. Остаток: {sequence["quantity"]}")

    @printing_products.setter
    def printing_products(self, new_product):
        """Создал сеттер для добавления нового продукта в список продуктов и проверяю, является ли он экземпляром класса
        Product или его дочерними классами, если нет то не добавляю"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
        else:
            print("")

    def __str__(self):
        """Вывожу данные в формате 'Название категории, количество продуктов: 200 шт.'"""
        # Считаю сколько товаров в категории
        quantity = 0
        for i in self.__products:
            quantity += i["quantity"]
        return f"{self.title}, количество продуктов:{quantity} шт."


class AbstractProduct(ABC):
    """Создал абстрактный класс для класса Product и его наследников"""
    @abstractmethod
    def __str__(self):
        """Добавил этот абстрактный метод чтобы был(для задания)"""
        pass


class Product(Mixin, ABC):
    """Класс имеет свойства: название, описание, цена(приватный) и количество в наличии"""
    def __init__(self, title, description, price, quantity_in_stock, colour=None):
        super().__init__(title, description, price, quantity_in_stock)
        self.title = title
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock
        self.colour = colour

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
         сумм, умноженных на количество на складе. При этом проверяя что товары складываются только из этого класса"""
        if type(self) == type(other):
            return self.__price * self.quantity_in_stock + other.__price * other.quantity_in_stock
        else:
            raise TypeError


class Smartphone(Product):
    """Создаю дочерний класс от класса Products и добавляю в него:
    efficiency - производительность
    model - модель
    amount_of_internal_memory - объем встроенной памяти
    colour - добавил в родительский класс"""
    def __init__(self, title, description, price, quantity_in_stock, efficiency, model, amount_of_internal_memory,
                 colour):
        super().__init__(title, description, price, quantity_in_stock, colour)
        self.efficiency = efficiency
        self.model = model
        self.amount_of_internal_memory = amount_of_internal_memory
        self.colour = colour

    def __str__(self):
        """Создал этот метод только для того чтобы было что-то общее с классом Product, чтобы абстрактный класс работал
        нормально"""
        return self.title


class LawnGrass(Product):
    """Создаю дочерний класс от класса Products и добавляю в него:
    country_of_origin - страна производитель
    germination_period - срок прорастания
    colour - добавил в родительский класс"""
    def __init__(self, title, description, price, quantity_in_stock, country_of_origin, germination_period, colour):
        super().__init__(title, description, price, quantity_in_stock, colour)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period

    def __str__(self):
        """Создал этот метод точно так же как в классе Smartphone"""
        return self.title


class Order(AbstractCategory):
    """Класс выводит  на экран информацию о купленном товаре, сколько купили и итоговую цену
    product: экземпляр класса Product или его дочерних классов
    quantity_of_purchased_product: сколько товара хотят приобрести"""
    def __init__(self, product, quantity_of_purchased_product):
        self.product = product
        self.quantity_of_purchased_product = quantity_of_purchased_product

    def __str__(self):
        """Вывожу то, что в описании класса"""
        return (f"куплен {self.product.title}, {self.quantity_of_purchased_product} шт, "
                f"{self.product.printing_price * int(self.quantity_of_purchased_product)}")
