from argparse import ArgumentParser

from django.contrib.auth import get_user_model
from django.db import transaction

from faker.exceptions import UniquenessException

from ..utils.base_command import GenerateDataCommand
from ..utils.table_util import TablesDataDictGenerator


class Command(GenerateDataCommand, TablesDataDictGenerator):
    """
    Generates number `count` entries and writes to DB.
    Creates `count` instances of User table.
    """
    def add_custom_arguments(self, parser: ArgumentParser):
        pass

    def generate_data(self, num_entries: int, **options):
        error_counter = 0

        for i in range(1, num_entries + 1):
            self.update_gender()

            # ensures that we make rollback
            # when any error during generating data
            with transaction.atomic():
                try:
                    # create user
                    get_user_model().objects.create(
                        **self.create_user()
                    )

                except UniquenessException:
                    # Catch Faker error and log it
                    error_counter += 1
                    self.stdout.write(
                        self.style.ERROR(
                            "Some fields `Faker` could not make unique. "
                            f"Moving to next entry!!!. Skipped: {error_counter}"
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
