from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Сыры', 'description': 'твердые'},
            {'name': 'Колбасы', 'description': 'Разные'},
            {'name': 'Молоко', 'description': 'Топленое'}

        ]

        category_added = []

        for item in category_list:
            category_added.append(
                Category(**item)
            )

        Category.objects.bulk_create(category_added)
