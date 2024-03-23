import pytest
from src.classes import Category, Product

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


# Тест на инициализацию Product
def test_init_product(product_test):
    assert product_test.title == "яблоко"
    assert product_test.description == "Сочное и вкусное"
    assert product_test.printing_price == 30.5
    assert product_test.quantity_in_stock == 12
