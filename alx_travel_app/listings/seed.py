from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = [
            "Seaside Villa",
            "Mountain Retreat",
            "Urban Apartment",
            "Desert Escape",
            "Countryside Cottage"
        ]
        locations = ["Cairo", "Alexandria", "Luxor", "Aswan", "Hurghada"]

        for i in range(10):  # create 10 listings
            Listing.objects.create(
                title=random.choice(titles),
                description="A wonderful place to stay.",
                location=random.choice(locations),
                price_per_night=random.uniform(50, 300),
                available=True
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings."))
