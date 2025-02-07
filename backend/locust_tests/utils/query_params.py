from abc import ABC, abstractmethod

from locust import FastHttpUser, tag, HttpUser

from locust_tests import (
    MAN_PAGE,
    WOMAN_PAGE,
    fake,
    HttpSessionType
)

from gevent import pool

from typing import Literal


def search(
        client: HttpSessionType,
        url: str,
        gender: Literal["man", "woman"] = "none",
):
    """
    Creates concurrent requests on `url?search=` using gevent
    :param client: Client from Locust
    :param url: URL path to endpoint
    :param gender: Gender decides what gender fullname will be
    :return:
    """
    def concurrent_request(
            client_: HttpSessionType,
            url_: str,
            query_param_url: str
    ):
        client_.get(
            url_ + query_param_url,
            name=f"{url_}/search"
        )

    genders = {
        "man": fake.name_male,
        "woman": fake.name_female,
        "none": fake.name,
    }

    request_pool = pool.Pool()
    for _ in range(5):
        full_name = genders[gender]()
        request_pool.spawn(
            concurrent_request,
            client,
            # base url, will be used in request grouping
            url,
            # search by not completed fullname
            f"?search={full_name[:len(full_name) // 2]}"
        )

    request_pool.join()


def min_max_numbers(
        offset: int,
        min_num: int,
        max_num: int,
) -> tuple[int, int]:
    """
    Returns tuple minimum number and maximum number,
    with positive range between max - min.
    :param offset: Difference we want to have in
    resulting max - min. Used to create range.
    :param min_num: Minimum range of number we are going to
    use to get random number in range `min_num + offset`
    :param max_num: Maximum range of number we are going to
    use to get random number in range `max_num - offset`

    :return:
    """
    min_number = fake.random_int(
        min=min_num, max=offset + min_num
    )
    max_number = fake.random_int(
        min=max_num - offset, max=max_num
    )

    return min_number, max_number


class FilterQuery(ABC):
    def __init__(self, field: str):
        self.field = field

    @abstractmethod
    def query_param(self) -> str:
        pass


class RangeFilterQuery(FilterQuery):
    """
    Class for building queries parameters for fields
    in Model like `height`, `bust`, 'hips', 'waist'. Query parameters which
    are required to have some range like min `height_min` and `height_max`
    """
    def __init__(
            self,
            field: str,
            offset: int,
            min_val: int,
            max_val: int,
    ):
        """
        :param offset: Difference we want to have in
        resulting max - min. Used to create range.
        :param field:
        :param min_val:
        :param max_val:
        """
        super().__init__(field)
        self.min_val = min_val
        self.max_val = max_val
        self.offset = offset

    def query_param(self) -> str:
        min_, max_ = min_max_numbers(
            offset=self.offset, max_num=self.max_val, min_num=self.min_val
        )
        return f"{self.field}_min={min_}&{self.field}_max={max_}"


class ChoiceFilterQuery(FilterQuery):
    """
    Class for building queries parameters for fields
    in Model like `hair`, `eye_color`, where user need to choose.
    """
    def __init__(
            self,
            field: str,
            choices: list[str]
    ):
        super().__init__(field)
        self.choices = choices

    def query_param(self) -> str:
        return f"{self.field}={fake.random_element(self.choices)}"


def filter_task(
        client: HttpSessionType,
        url: str,
        filters: list[FilterQuery]
):
    """
    Locust filter task, creates query parameters using
    FilterQuery.query_param.
    :param client: Session
    :param url: URL to endpoint
    :param filters: list of FilterQuery base class
    :return:
    """
    query_params = "?"
    for filter_q in filters:
        query_params += filter_q.query_param() + "&"

    client.get(
        url + query_params.rstrip("&"),
        name=f"{url}/filters"
    )


def add_filter_locust_task(
        user_class: FastHttpUser | HttpUser,
        url: str,
        filters: list[FilterQuery],
        task_name_suffix: str,
        tag_name: str = "model_filters"
) -> str:
    """

    :param user_class:
    :param url:
    :param filters:
    :param task_name_suffix:
    :param tag_name:
    :return:
    """
    def locust_task(self):
        filter_task(
            client=self.client,
            url=url,
            filters=filters
        )

    # locust task method name
    func_name = f"{url.replace('/', '_')}_{task_name_suffix}"
    locust_task.__name__ = f"filter_by_{func_name}"

    # append new Locust task to user_class
    user_class.tasks.append(tag(tag_name)(locust_task))

    return locust_task.__name__


hair_choices = ["blonde", "brown", "black", "red", "grey", "other"]
eye_color_choices = ["blue", "green", "brown", "gray", "hazel"]

# Man and Woman pages have same filters, and I did not want duplicate code.
# That why I separated query filters on classes like `RangeFilterQuery` and
# `ChoiceFilterQuery`. Allowing us to dictate the behaviour of filter logic.
# Each value in  MAN_TASKS_FILTERS and WOMAN_TASKS_FILTERS is separate Locust
#  task. We can set more filter fields in one Locust task,
# by using one of FilterQuery subclasses
MAN_TASKS_FILTERS = [
    (MAN_PAGE, [RangeFilterQuery("height", 30, 140, 220)]),
    (MAN_PAGE, [RangeFilterQuery("bust", 5, 35, 50)]),
    (MAN_PAGE, [RangeFilterQuery("hips", 5, 35, 50)]),
    (MAN_PAGE, [RangeFilterQuery("waist", 5, 25, 45)]),
    (MAN_PAGE, [ChoiceFilterQuery("hair", hair_choices)]),
    (MAN_PAGE, [ChoiceFilterQuery("eye_color", eye_color_choices)]),
]

WOMAN_TASKS_FILTERS = [
    (WOMAN_PAGE, [RangeFilterQuery("height", 30, 140, 220)]),
    (WOMAN_PAGE, [RangeFilterQuery("bust", 20, 70, 120)]),
    (WOMAN_PAGE, [RangeFilterQuery("hips", 30, 50, 90)]),
    (WOMAN_PAGE, [RangeFilterQuery("waist", 20, 60, 120)]),
    (WOMAN_PAGE, [ChoiceFilterQuery("hair", hair_choices)]),
    (WOMAN_PAGE, [ChoiceFilterQuery("eye_color", eye_color_choices)]),
]

FILTER_TASKS = MAN_TASKS_FILTERS + WOMAN_TASKS_FILTERS
