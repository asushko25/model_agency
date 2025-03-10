from argparse import ArgumentParser

import logging
from locust import (
    FastHttpUser,
    task,
    between,
    tag,
    events
)
from locust.env import Environment
from locust.runners import WorkerRunner

from locust_tests.utils.query_params import (
    search,
    FILTER_TASKS,
    add_filter_locust_task
)
from locust_tests.utils.common import (
    get_detail_url_from_model,
    contact_agency_about_model
)

import requests

from locust_tests import (
    MAIN_PAGE,
    MAN_PAGE,
    WOMAN_PAGE,
    CONTACT_PAGE,

    MODEL_DETAIL_GROUP,

    PHONE_NUMBER,
    HOST,
    LIMIT,
    fake
)


@events.init_command_line_parser.add_listener
def _(parser: ArgumentParser):
    """Add custom CLI arguments"""
    # Args for `DoubleWave` test shape load
    parser.add_argument(
        "--min-users", type=int, default=20,
        help="Minimum number of users at start for DoubleWave shape class"
    )
    parser.add_argument(
        "--peak-one-users", type=int, default=80,
        help="Number of users on first peak for DoubleWave shape class"
    )
    parser.add_argument(
        "--peak-two-users", type=int, default=120,
        help="Number of users on second peak for DoubleWave shape class"
    )

    # Args for `StepLoadShape` test shape load

    parser.add_argument(
        "--step_time", type=int, default=30,
        help="Time between steps for StepLoadShape shape class"
    )
    parser.add_argument(
        "--step_load", type=int, default=10,
        help="User increase amount at each step for StepLoadShape shape class"
    )
    parser.add_argument(
        "--spawn_rate", type=int, default=10,
        help=(
            "Users to stop/start per second at every step"
            " for StepLoadShape shape class"
        )
    )

    # Common argument
    parser.add_argument(
        "--time-limit", type=int, default=600, help="Limit time for test"
    )


@events.test_start.add_listener
def add_args_to_custom_load_shapes(environment: Environment, **kwargs):
    """Add arguments to locust_tests/shape_classes/ Custom Test Load Shapes"""
    options = environment.parsed_options
    shape_class = environment.shape_class

    if shape_class.__class__.__name__ == "DoubleWave":

        # set class attributes
        shape_class.min_users = options.min_users
        shape_class.peak_one_users = options.peak_one_users
        shape_class.peak_two_users = options.peak_two_users
        shape_class.time_limit = options.time_limit

    if shape_class.__class__.__name__ == "StepLoadShape":

        # set class attributes
        shape_class.step_time = options.step_time
        shape_class.step_load = options.step_load
        shape_class.spawn_rate = options.spawn_rate
        shape_class.time_limit = options.time_limit


@events.init.add_listener
def pagination_util(environment: Environment, **kwargs):
    """
    Get total number of entries on MAIN_PAGE, WOMAN_PAGE, MAN_PAGE,
    to be able to work with pagination, not only with 1 page
    :param environment:
    :param kwargs:
    :return:
    """

    if isinstance(environment.runner, WorkerRunner):
        try:
            main_page = requests.get(HOST + MAIN_PAGE)
            setattr(
                TestModels, "total_main_models",
                main_page.json().get("count", 0)
            )

            man_page = requests.get(HOST + MAN_PAGE)
            setattr(
                TestModels, "total_man_models",
                man_page.json().get("count", 0)
            )

            woman_page = requests.get(HOST + WOMAN_PAGE)
            setattr(
                TestModels, "total_woman_models",
                woman_page.json().get("count", 0)
            )
        except requests.RequestException as e:
            logging.error(
                f"Could not get total number of entries at"
                f" {pagination_util.__name__} locust event: {e}"
            )


@events.init.add_listener
def app_filter_tasks(environment: Environment, **kwargs):
    if isinstance(environment.runner, WorkerRunner):
        logging.info(
            f"{environment.runner}: Initiating filter tasks defined"
            f" in `./utils/query_params.py`"
        )
        for url, filter_query in FILTER_TASKS:
            task_name_suffix = "_".join(
                filter_.field for filter_ in filter_query
            )
            add_filter_locust_task(
                user_class=TestModels,
                url=url,
                filters=filter_query,
                task_name_suffix=task_name_suffix
            )


class TestModels(FastHttpUser):
    host = HOST
    wait_time = between(2, 5)

    # this attributes used for pagination
    # no need for setting manually
    # locust event `pagination_util` will set values
    total_main_models = 0
    total_man_models = 0
    total_woman_models = 0

    @tag("model-list")
    @task
    def main_page(self):
        query_param = (
            f"?limit={LIMIT}"
            f"&offset={fake.pyint(LIMIT, self.total_main_models)}"
        )
        self.client.get(
            MAIN_PAGE + query_param, name=MAIN_PAGE
        )

    @tag("model-search")
    @task
    def search_on_main_page(self):
        search(
            url=MAIN_PAGE,
            client=self.client,
        )

    @tag("model-list")
    @task
    def man_model_page(self):
        query_param = (
            f"?limit={LIMIT}"
            f"&offset={fake.pyint(LIMIT, self.total_man_models)}"
        )
        self.client.get(
            MAN_PAGE + query_param, name=MAN_PAGE
        )

    @tag("model-search")
    @task
    def search_man_page(self):
        search(
            client=self.client,
            url=MAN_PAGE,
            gender="man"
        )

    @tag("model-list")
    @task
    def woman_model_page(self):
        query_param = (
            f"?limit={LIMIT}"
            f"&offset={fake.pyint(LIMIT, self.total_woman_models)}"
        )
        self.client.get(
            WOMAN_PAGE + query_param, name=WOMAN_PAGE
        )

    @tag("model-search")
    @task
    def search_woman_page(self):
        search(
            client=self.client,
            url=WOMAN_PAGE,
            gender="woman"
        )

    @tag("model-detail")
    @task
    def model_detail_page_start_on_main_page(self):
        self.client.get(get_detail_url_from_model(
            user=self, url=MAIN_PAGE), name=MODEL_DETAIL_GROUP
        )

    @tag("model-detail")
    @task
    def model_detail_page_start_on_man_page(self):
        self.client.get(get_detail_url_from_model(
            user=self, url=MAN_PAGE), name=MODEL_DETAIL_GROUP
        )

    @tag("model-detail")
    @task
    def model_detail_page_start_on_woman_page(self):
        self.client.get(get_detail_url_from_model(
            user=self, url=WOMAN_PAGE), name=MODEL_DETAIL_GROUP
        )

    @tag("model-contact")
    @task
    def contact_page(self):
        json_data = {
            "name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.free_email(),
            "phone_number": PHONE_NUMBER,
            "message": fake.text()
        }
        with self.rest("POST", CONTACT_PAGE, json=json_data):
            pass

    @tag("model-contact")
    @task
    def contact_about_model_through_main_page(self):
        detail_url = get_detail_url_from_model(
            user=self, url=MAIN_PAGE
        )
        contact_agency_about_model(
            user=self, detail_url=detail_url
        )

    @tag("model-contact")
    @task
    def contact_about_model_through_man_page(self):
        detail_url = get_detail_url_from_model(
            user=self, url=MAN_PAGE
        )
        contact_agency_about_model(
            user=self, detail_url=detail_url
        )

    @tag("model-contact")
    @task
    def contact_about_model_through_woman_page(self):
        detail_url = get_detail_url_from_model(
            user=self, url=WOMAN_PAGE
        )
        contact_agency_about_model(
            user=self, detail_url=detail_url
        )


if __name__ == "__main__":
    from locust import run_single_user

    run_single_user(TestModels)
