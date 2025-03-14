import faker
from pathlib import Path

from django.contrib.auth import get_user_model

fake = faker.Faker()


class ModelsTableDataDictGenerator:
    """
    Class which generates models table data like dictionary
    Using `Faker` for generating fake data.
    """

    gender = "man"
    man_images_paths = None
    woman_images_paths = None

    path_to_man_images = "core/management/utils/test_images/man"
    path_to_woman_images = "core/management/utils/test_images/woman"

    def update_gender(self):
        """
        Data will be separated by gender half woman and half man
        """
        swap = {
            "woman": "man",
            "man": "woman",
        }
        self.gender = swap[self.gender]

    def create_user(self) -> dict:
        """Creates User table dict data"""
        return {
            "is_superuser": False,
            "is_staff": False,
            "is_active": False,
            "full_name": (
                fake.name_male()
                if self.gender == "man"
                else fake.name_female()
            ),
            "email": fake.unique.free_email()
        }

    def create_model(self, user: get_user_model):
        """
        Creates Model table dict data with a given user id
        """
        hair_choices = ["blonde", "brown", "black", "red", "grey", "other"]
        eye_color_choices = ["blue", "green", "brown", "gray", "hazel"]

        bust = fake.pyint(80, 120)
        waist = fake.pyint(60, 100)
        hips = fake.pyint(80, 120)

        while waist > bust and waist > hips:
            waist = fake.pyint(60, min(bust, hips))

        return {
            "model_user": user,
            "date_of_birth": fake.date_of_birth(
                minimum_age=18,
                maximum_age=40
            ),
            "city": fake.city(),
            "country": fake.country(),
            "height": fake.pyint(160, 190),
            "hair": fake.random_element(hair_choices),
            "eye_color": fake.random_element(eye_color_choices),
            "gender": self.gender,
            "bust": bust,
            "waist": waist,
            "hips": hips,
        }

    def create_man_images_paths(self):
        """Get Test Man images paths"""
        if not self.man_images_paths:
            images_path = Path(self.path_to_man_images)
            self.man_images_paths = [
                str(file) for file in images_path.iterdir() if file.is_file()
            ]

    def create_woman_images_paths(self):
        """Get Test Woman images paths"""
        if not self.woman_images_paths:
            images_path = Path(self.path_to_woman_images)
            self.woman_images_paths = [
                str(file) for file in images_path.iterdir() if file.is_file()
            ]

    def get_image_path(self):
        """
        Returns random image paths from woman_images_paths or
        man_images_paths, depends on `gender` from which list we will
        take
        """
        if not self.man_images_paths:
            self.create_man_images_paths()

        if not self.woman_images_paths:
            self.create_woman_images_paths()

        return (
            fake.random_element(self.man_images_paths)
            if self.gender == "man"
            else fake.random_element(self.woman_images_paths)
        )


class NewsletterTableDataGenerator:
    newsletter_images_paths = None
    path_to_newsletter_images = "core/management/utils/test_images/newsletters"

    def create_newsletter(self) -> dict:
        """Creates Newsletter table dict data"""
        return {
            "header": fake.sentence(nb_words=10),
            "cover": "",
            "caption": fake.sentence(nb_words=20)
        }

    def create_newsletter_images_paths(self):
        """Get Test Man images paths"""
        if not self.newsletter_images_paths:
            images_path = Path(self.path_to_newsletter_images)
            self.newsletter_images_paths = [
                str(file) for file in images_path.iterdir() if file.is_file()
            ]

    def get_newsletter_image_path(self):
        """
        Returns random image paths from newsletter_images_paths
        so we could create even more newsletter then number of
        newsletter images in core.management.utils.test_images.newsletters
        """
        if not self.newsletter_images_paths:
            self.create_newsletter_images_paths()

        return fake.random_element(self.newsletter_images_paths)
