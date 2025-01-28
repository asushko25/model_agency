from argparse import ArgumentParser

from django.core.files import File
from django.contrib.auth import get_user_model
from django.db import transaction

from faker.exceptions import UniquenessException

from ..utils.base_command import GenerateDataCommand
from ..utils.table_util import TablesDataDictGenerator

from model.models import (
    Model,
    ModelImages
)


class Command(GenerateDataCommand, TablesDataDictGenerator):
    """
    Generates number `num_entries` entries and writes to DB.
    Creates `num_entries` instances of Model table together with User table.
    """
    def add_custom_arguments(self, parser: ArgumentParser):
        parser.add_argument(
            "--model_image",
            action="store_true",
            help=(
                "Flag indicates creating Model table entries, "
                "together with User table, with model images"
            )
        )

    def set_model_image(self, model_id: Model):
        image_path = self.get_image_path()

        with open(image_path, "rb") as f:
            django_file = File(f)

            ModelImages.objects.create(
                image=django_file,
                model_id=model_id,
                caption=""
            )

    def generate_data(self, num_entries: int, **options):
        error_counter = 0

        for i in range(1, num_entries + 1):
            self.update_gender()

            # ensures that we make rollback
            # when any error during generating data
            with transaction.atomic():
                try:
                    # create user
                    user = get_user_model().objects.create(
                        **self.create_user()
                    )
                    # create model from user
                    model = Model.objects.create(
                        **self.create_model(user_id=user.id)
                    )
                    # if `model_image` is provided.
                    # Set image for model
                    if options.get("model_image"):
                        self.set_model_image(model_id=model.id)

                except UniquenessException as er:
                    # Catch Faker error and log it
                    error_counter += 1
                    self.stdout.write(
                        self.style.ERROR(
                            "Some fields `Faker` could not make unique. "
                            f"Moving to next entry!!!. Skipped: {error_counter}. \n"
                            f"Error: {er}"
                        )
                    )

                    transaction.set_rollback(True)

                except Exception as e:
                    # catch rest of errors without stoping creating
                    error_counter += 1
                    self.stdout.write(
                        self.style.ERROR(f"Error: {str(e)}. Skipped: {error_counter}")
                    )

                    transaction.set_rollback(True)

        self.stdout.write(
            self.style.SUCCESS(
                f"User entries where successfully created."
                f" Number of entries created: {num_entries - error_counter}"
                f" and {error_counter} skipped."
            )
        )

    def custom_handler(self, num_entries: int, **options):
        self.generate_data(num_entries=num_entries, **options)
