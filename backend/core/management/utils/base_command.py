from argparse import ArgumentParser
from abc import ABC, abstractmethod

from django.core.management.base import (
    BaseCommand,
)


class GenerateDataCommand(BaseCommand, ABC):
    help = (
        "Generates `-c` or `--count` number of entries of data,"
        " default = 100. "
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
        This method should be overridden in subclasses to
        add their own arguments.
        :param parser: ArgumentParse
        :return:
        """
        pass

    @abstractmethod
    def custom_handler(self, num_entries: int, **options):
        pass

    def handle(self, *args, **options):
        """
        Can be used only in development or staging environment.
        :param args:
        :param options:
        :return:
        """
        num_entries = options.pop("num_entries")

        self.custom_handler(num_entries=num_entries, **options)

    def add_arguments(self, parser: ArgumentParser):
        """
        This method should be overridden in subclasses to
        add their own arguments.
        :param parser: ArgumentParse
        :return:
        """
        parser.add_argument(
            "-n_e",
            "--num_entries",
            type=int,
            default=0,
            help="Number of entries generated, default = 100",
        )

        self.add_custom_arguments(parser=parser)
