from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'id': 1, 'name': 'Сыры', 'description': 'твердые'},
            {'id': 2, 'name': 'Колбасы', 'description': 'Разные'},
            {'id': 3, 'name': 'Молоко', 'description': 'Топленое'}

        ]

        category_added = []

        product_list = [
            {'name': 'Пармезан', 'description': 'Твердые', 'category_id': 1, 'price': '303.20',
             'date_of_creation': '2023-07-23'},
            {'name': 'Домик в деревне', 'description': 'Свежее', 'category_id': 3, 'price': '50.20',
             'date_of_creation': '2023-07-23'},
            {'name': 'Простоквашино', 'description': 'Топленое', 'category_id': 3, 'price': '77.25',
             'date_of_creation': '2023-07-23'}

        ]

        product_added = []

        for item in category_list:
            category_added.append(
                Category(**item)
            )

        for item in product_list:
            product_added.append(
                Product(**item)
            )

        Category.objects.bulk_create(category_added)

        Product.objects.bulk_create(product_added)
