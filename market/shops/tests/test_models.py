from django.test import TestCase
from shops.models import Shop, Offer
from products.models import Product, Property, Category


class ShopModelTest(TestCase):
    """Класс тестов модели Магазин"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.property = Property.objects.create(name='тестовая характеристика')
        cls.category = Category.objects.create(name='тестовая категория', description='тестовое описание категории')
        cls.product = Product.objects.create(
            name='Тестовый продукт',
            category=cls.category
        )
        cls.product.property.set([cls.property])
        cls.shop = Shop.objects.create(name='тестовый магазин')
        cls.offer = Offer.objects.create(shop=cls.shop, product=cls.product, price=25)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        ShopModelTest.property.delete()
        ShopModelTest.product.delete()
        ShopModelTest.shop.delete()
        ShopModelTest.offer.delete()

    def test_verbose_name(self):
        shop = ShopModelTest.shop
        field_verboses = {
            'name': 'название',
            'products': 'товары в магазине',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(shop._meta.get_field(field).verbose_name, expected_value)

    def test_name_max_length(self):
        shop = ShopModelTest.shop
        max_length = shop._meta.get_field('name').max_length
        self.assertEqual(max_length, 512)


class OfferModelTest(TestCase):
    """Класс тестов модели Предложение магазина"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name='тестовая категория', description='тестовое описание категории')
        cls.product = Product.objects.create(
            name='Тестовый продукт',
            category=cls.category
        )
        cls.shop = Shop.objects.create(name='тестовый магазин')
        cls.offer = Offer.objects.create(shop=cls.shop, product=cls.product, price=35)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        OfferModelTest.product.delete()
        OfferModelTest.shop.delete()
        OfferModelTest.offer.delete()

    def test_verbose_name(self):
        offer = OfferModelTest.offer
        field_verboses = {
            'price': 'цена',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(offer._meta.get_field(field).verbose_name, expected_value)

    def test_price_max_digits(self):
        offer = OfferModelTest.offer
        max_digits = offer._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 10)

    def test_price_decimal_places(self):
        offer = OfferModelTest.offer
        decimal_places = offer._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)
