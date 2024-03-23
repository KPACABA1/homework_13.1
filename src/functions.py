import json


def reading_a_file():
    """Создаю функцию для возврата Paython списка из файла  для дальнейшего присвоения данных к классам"""
    with open("../src/products.json", "rt", encoding='utf-8') as products_json:
        products_python = json.load(products_json)
        return products_python
