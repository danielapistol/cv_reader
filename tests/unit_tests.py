from unittest.mock import patch

import pytest

from app import app
from models.cv_models import PersonContact

app = app.test_client()


@pytest.mark.parametrize("age,expected_result", [(25, 200), (159, 400), (None, 200)])
def test_get_personal_info(age, expected_result):
    # pytest.set_trace()
    with patch(
        "app.cv_data.data",
        {
            "contact": {
                "name": "Daniela Pistol",
                "mail": "danapistol@flask.com",
                "phone": "+33123456789",
                "age": age,
                "location": {
                    "address": "2 rue Paradis",
                    "postal_code": "75010",
                    "city": "Paris",
                    "country": "FR",
                    "region": "France",
                },
            },
        },
    ):
        response = app.get("/personal")
        data = response.get_json()
        assert response.status_code == expected_result
        if expected_result == 200:
            assert PersonContact(**data)
            assert age is None or age > 18 or age < 120


@pytest.mark.parametrize("expected_result", [404])
def test_get_personal_info(expected_result):
    response = app.get("/contact")
    assert response.status_code == expected_result
