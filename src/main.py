from functions import reading_a_file
from classes import Category, Product, Smartphone, LawnGrass

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

# Создаю новый товар(Смартфоны) от родительского класса Product
product_smartphone = Smartphone("Nokia", "Бронированный телефон", 12000, 20,
                                "2 GB", "SX4", "32 GB", "Black")

# Создаю ещё 1 новый товар(Газонная трава) от родительского класса Product
product_lawn_grass = LawnGrass("White clover", "Один из самых лучших сортов газонной травы", 2500,
                               13, "Russia", "13 дней", "Green")




