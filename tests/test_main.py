import pytest
from src.classes import Category, Product
from src.classes import Smartphone, LawnGrass


# Фикстура для теста инициализации Category
@pytest.fixture()
def category_test():
    return Category("Фрукты", "Сочные и вкусные", ["Яблоко"])


# Тест для инициализации Category
def test_init_category(category_test):
    assert category_test.title == "Фрукты"
    assert category_test.description == "Сочные и вкусные"
    assert category_test.total_number_of_categories == 1
    assert category_test.total_number_of_unique_products == 1


# Фикстура для теста на инициализацию Product
@pytest.fixture()
def product_test():
    return Product("яблоко", "Сочное и вкусное", 30.5, 12)


# Фикстура для теста метода __add__ в классе Product
@pytest.fixture()
def product_test_2():
    return Product("Яйца", "Свежие", 10, 20)


# Тест на инициализацию Product
def test_init_product(product_test):
    assert product_test.title == "яблоко"
    assert product_test.description == "Сочное и вкусное"
    assert product_test.printing_price == 30.5
    assert product_test.quantity_in_stock == 12


# Тест на функционал класса Product
def test_product(product_test, product_test_2):
    assert product_test + product_test_2 == 566


# Фикстура для теста инициализации класса Smartphone
@pytest.fixture()
def smartphone_test():
    return Smartphone("Honor", "Топ за свои деньги", 25000, 18, "2 GB",
                      "ZYT1", "128GB", "Black")


# Тест для инициализации Smartphone
def test_init_smartphone(smartphone_test):
    assert smartphone_test.title == "Honor"
    assert smartphone_test.description == "Топ за свои деньги"
    assert smartphone_test.printing_price == 25000
    assert smartphone_test.quantity_in_stock == 18
    assert smartphone_test.efficiency == "2 GB"
    assert smartphone_test.model == "ZYT1"
    assert smartphone_test.amount_of_internal_memory == "128GB"
    assert smartphone_test.colour == "Black"


# Фикстура для теста инициализации класса LawnGrass
@pytest.fixture()
def lawn_grass_test():
    return LawnGrass("Green_s", "Зеленее некуда", 1200, 32, "Russia",
                     "12 days", "green")


# Тест на инициализацию класса LawnGrass
def test_init_lawn_grass(lawn_grass_test):
    assert lawn_grass_test.title == "Green_s"
    assert lawn_grass_test.description == "Зеленее некуда"
    assert lawn_grass_test.printing_price == 1200
    assert lawn_grass_test.quantity_in_stock == 32
    assert lawn_grass_test.country_of_origin == "Russia"
    assert lawn_grass_test.germination_period == "12 days"
    assert lawn_grass_test.colour == "green"
