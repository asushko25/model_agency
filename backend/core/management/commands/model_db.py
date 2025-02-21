from argparse import ArgumentParser

from django.contrib.auth import get_user_model
from django.db import transaction
from django.core.files.base import ContentFile

from faker.exceptions import UniquenessException

from ..utils.base_command import GenerateDataCommand
from ..utils.table_util import ModelsTableDataDictGenerator

from model.models import Model, ModelImages


class Command(GenerateDataCommand, ModelsTableDataDictGenerator):
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
            ),
        )

    def get_model_image(self, model: Model) -> ModelImages:
        image_path = self.get_image_path()

        with open(image_path, "rb") as f:
            image_content = f.read()

        return ModelImages(
            image=ContentFile(image_content, name="temp_image.jpg"),
            model=model,
            caption=""
        )

    def generate_data(self, num_entries: int, **options):
        error_counter = 0
        # number of objects in one package
        batch_size = 1000
        models = []
        users = []
        model_images = []

        def perform_bulk_create():
            with transaction.atomic():
                get_user_model().objects.bulk_create(users)
                Model.objects.bulk_create(models)

                if options.get("model_image"):
                    ModelImages.objects.bulk_create(model_images)

        for i in range(1, num_entries + 1):
            self.update_gender()

            try:
                # create user
                user = get_user_model()(**self.create_user())
                users.append(user)

                # create model from user
                model = Model(
                    **self.create_model(user=user)
                )
                models.append(model)
                # if `model_image` is provided.
                # Set image for model
                if options.get("model_image"):
                    model_images.append(self.get_model_image(model))

            except UniquenessException as er:
                # Catch Faker error and log it
                error_counter += 1
                self.stdout.write(
                    self.style.ERROR(
                        "Some fields `Faker` could not make unique. "
                        "Moving to next entry!!!."
                        f" Skipped: {error_counter}. \n"
                        f"Error: {er} "
                        f"Left to create: {num_entries - i}"
                    )
                )

            except Exception as e:
                # catch rest of errors without stoping creating
                error_counter += 1
                self.stdout.write(
                    self.style.ERROR(
                        f"Error: {str(e)}. Skipped: {error_counter} "
                        f"Left to create: {num_entries - i}"
                    )
                )

            if len(users) > batch_size:
                perform_bulk_create()
                users.clear()
                models.clear()
                model_images.clear()

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
