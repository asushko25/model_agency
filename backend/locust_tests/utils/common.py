from locust import FastHttpUser

from locust_tests import (
    MODEL_DETAIL_GROUP,
    CONTACT_MODEL_GROUP,
    PHONE_NUMBER
)
from locust_tests import (
    fake,
)


def get_detail_url_from_model(
        user: FastHttpUser,
        url: str,
):
    """
    User request `url` page models, then choosing random model from model list,
    getting `detail_url` from chosed model, and returning model detail url.

    :param user:
    :param url:
    :param request_name: Grouping requests with the name `request_name`
    :return:
    """
    with user.rest("GET", url) as resp:
        if not resp.js:
            return

        # check if pagination is ON or Not
        model_list = resp.js.get("results") or resp.js

        if not model_list:
            # there are should be models on every url
            resp.failure(f"There are no models on: {url}")
            return

        # random model detail URL from response on Main page
        detail_url = fake.random_element(model_list).get("detail_url")
        if not detail_url:
            resp.failure(
                "List of Models JSON does not have `detail_url`"
            )
            return

    return detail_url


def contact_agency_about_model(
        user: FastHttpUser,
        detail_url: str,
):
    """
    User request `url` page models, then choosing random model from model list,
    getting `detail_url` from chosed model, and requesting model detail url.
    From model detail url we are returning to contact page.
    Result we are mimic client contacting agency about model,
    starting from Main page.
    :param user:
    :param detail_url: API endpoint to Model detail page
    :return:
    """
    with user.rest("GET", detail_url, name=MODEL_DETAIL_GROUP) as resp:
        if not resp.js:
            return

        # getting from detail JSON field `contact_url`
        # to redirect to contact page with model id
        contact_url = resp.js.get("contact_url")
        if not contact_url:
            resp.failure(
                f"Model detail url: {detail_url}, "
                "should have in JSON response field `contact_url`"
            )
            return

    json_data = {
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.free_email(),
        "phone_number": PHONE_NUMBER,
        "message": fake.text()
    }

    with user.rest("POST", contact_url, json=json_data, name=CONTACT_MODEL_GROUP):
        pass
