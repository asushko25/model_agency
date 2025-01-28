import os

from argparse import ArgumentParser
from abc import ABC, abstractmethod

from django.core.management.base import (
    BaseCommand,
)
from django.contrib.auth import get_user_model


class GenerateDataCommand(BaseCommand, ABC):
    help = (
        "Generates `-c` or `--count` number of entries of data, default = 100. "
        "Starting from tables User, Model, ModelImage. "
        "Fulfilling all fields data using `Faker` and model images"
    )

    @abstractmethod
    def generate_data(self, num_entries: int, **options):
        """Generates Data in and writes it to format you need"""
        pass

    @abstractmethod
    def add_custom_arguments(self, parser: ArgumentParser):
        """
        This method should be overridden in subclasses to add their own arguments.
        :param parser: ArgumentParse
        :return:
        """
        pass

    @abstractmethod
    def custom_handler(self, num_entries: int, **options):
        pass

    def flush_db_users(self):
        """
        Deletes all users from DB and maybe records with on_delete=CASCADE.
        Can be used only in development or staging environment.
        Saves admins, for safety reasons.
        """
        debug_var = os.getenv("DJANGO_ENV")

        #  check if we on developing or staging environment
        allowed = any(
            [debug_var.startswith("prod"), debug_var.startswith("devel")]
        )

        if allowed:
            self.stdout.write(
                self.style.WARNING("Removing Users, except admin Users")
            )
            get_user_model().objects.filter(is_superuser=False).delete()

            return

        self.stdout.write(
            self.style.WARNING("You can't use this flag in current environment")
        )

    def handle(self, *args, **options):
        num_entries = options.pop("num_entries")
        flush_users = options.pop("flush_users")

        if flush_users:
            self.flush_db_users()

        self.custom_handler(
            num_entries=num_entries,
            **options
        )

    def add_arguments(self, parser: ArgumentParser):
        """
        This method should be overridden in subclasses to add their own arguments.
        :param parser: ArgumentParse
        :return:
        """
        parser.add_argument(
            "-n_e",
            "--num_entries",
            type=int,
            default=0,
            help="Number of entries generated, default = 100"
        )
        parser.add_argument(
            "--flush_users",
            action="store_true",
            default=False,
            help="Flushes all users from DB,"
                 " except saves admin Users"
        )
        self.add_custom_arguments(parser=parser)
