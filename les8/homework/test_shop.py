"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from .models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert Product.check_quantity(product, 10) == True
        assert Product.check_quantity(product, 1001) == False


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy

        first_quantity = product.quantity
        product.buy(10)
        assert  product.quantity == first_quantity - 10


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        try:
            product.buy(1001)  # Пытаемся купить больше, чем осталось
            assert False, "Должно было выброситься исключение ValueError"
        except ValueError:
            # Исключение выброшено - это правильно
            pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product):
        # тест добавления в корзину товара
        # создание корзины
        cart = Cart()
        # добавления товара в корзину
        cart.add_product(product, 1)

        # проверка наличия товара в корзине
        assert product in cart.products
        assert cart.products[product] == 1

        # дополнительная добавка товара
        cart.add_product(product, 2)
        # проверка кол-ва товара в корзине
        assert cart.products[product] == 3


    def test_remove_product(self, product):
        #Тест удаления товара из корзины
        cart = Cart()

        # добавляется в корзину 3, убирается 2, должен остаться 1
        cart.add_product(product, 3)
        cart.remove_product(product,2)
        assert cart.products[product] == 1

        # не передано кол-во, должно все удалиться
        cart.remove_product(product)
        assert product not in cart.products

        # добавляется в корзину 3, убирается 3, должно удалится
        cart.add_product(product, 3)
        cart.remove_product(product, 3)
        assert product not in cart.products

        # добавляется в корзину 1, убирается 3, должно удалится
        cart.add_product(product, 1)
        cart.remove_product(product, 3)
        assert product not in cart.products


    def test_clear(self, product):
        # тест очистки корзины
        cart = Cart()
        cart.add_product(product, 3)

        # очистка корзины
        cart.clear()
        assert product not in cart.products

    def test_get_total_price(self, product):
        # проверка суммы в корзине
        # цена товара 100
        cart = Cart()
        cart.add_product(product, 3)

        cart.get_total_price()
        # должно быть 300
        assert cart.get_total_price() == 300

    def test_buy(self, product):
        # проверка покупки из корзины
        cart = Cart()
        card_quantity = 3
        sklad_quantity = product.quantity

        cart.add_product(product, 3)

        cart.buy()

        # проверка вычитания со склада
        assert product.quantity == sklad_quantity - card_quantity

        # финальная проверка пустой корзины
        assert product not in cart.products

        # проверка ошибки в товаре > склада
        cart.add_product(product, 1001)
        try:
            cart.buy()  # Пытаемся купить больше, чем осталось
            assert False, "Должно было выброситься исключение ValueError"
        except ValueError:
            # Исключение выброшено - это правильно
            pass