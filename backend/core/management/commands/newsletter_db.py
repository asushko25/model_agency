from argparse import ArgumentParser

from django.db import transaction
from django.core.files.base import ContentFile

from ..utils.base_command import GenerateDataCommand
from ..utils.table_util import NewsletterTableDataGenerator

from newsletter.models import NewsLetter


class Command(GenerateDataCommand, NewsletterTableDataGenerator):
    """
    Generates number `num_entries` entries and writes to DB.
    Creates `num_entries` instances of Newsletter table.
    """

    def add_custom_arguments(self, parser: ArgumentParser):
        parser.add_argument(
            "--newsletter_image",
            action="store_true",
            help=(
                "Flag indicates creating Newsletter table entries, "
                "together with newsletter images"
            ),
        )

    def set_newsletter_image(self, newsletter: NewsLetter) -> NewsLetter:
        image_path = self.get_newsletter_image_path()

        with open(image_path, "rb") as f:
            image_content = f.read()

        newsletter.cover = ContentFile(image_content, name="temp_image.jpg")

        return newsletter

    def generate_data(self, num_entries: int, **options):
        error_counter = 0
        # number of objects in one package
        batch_size = 1000
        newsletters = []

        def perform_bulk_create():
            with transaction.atomic():
                NewsLetter.objects.bulk_create(newsletters)

        for i in range(1, num_entries + 1):
            try:
                # create user
                newsletter = NewsLetter(**self.create_newsletter())
                newsletters.append(newsletter)

                if options.get("newsletter_image"):
                    self.set_newsletter_image(newsletter)

            except Exception as e:
                # catch rest of errors without stoping creating
                error_counter += 1
                self.stdout.write(
                    self.style.ERROR(
                        f"Error: {str(e)}. Skipped: {error_counter} "
                        f"Left to create: {num_entries - i}"
                    )
                )

            if len(newsletters) > batch_size:
                perform_bulk_create()
                newsletters.clear()

        # perform the bulk_create for any remaining objects
        perform_bulk_create()

        self.stdout.write(
            self.style.SUCCESS(
                f"User entries where successfully created."
                f" Number of entries created: {num_entries - error_counter}"
                f" and {error_counter} skipped."
            )
        )

    def custom_handler(self, num_entries: int, **options):
        self.generate_data(num_entries=num_entries, **options)
