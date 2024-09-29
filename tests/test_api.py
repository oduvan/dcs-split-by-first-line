import pytest

from django.test import Client
from django.contrib.auth import get_user_model

from content_settings.models import ContentSetting

pytestmark = [pytest.mark.django_db(transaction=True)]


def get_anonymous_client():
    return Client()


def get_authenticated_client():
    user, created = get_user_model().objects.get_or_create(username="testuser")
    if created:
        user.set_password("testpassword")
        user.save()
    client = Client()
    client.login(username="testuser", password="testpassword")
    return client


def get_staff_client():
    user, created = get_user_model().objects.get_or_create(
        username="teststaff", is_staff=True
    )
    if created:
        user.set_password("testpassword")
        user.save()
    client = Client()
    client.login(username="teststaff", password="testpassword")
    return client


def test_get_simple_text():
    client = get_anonymous_client()

    resp = client.get("/books/fetch/main/")
    assert resp.status_code == 200
    assert resp.json()["COMPANY_DESCRIPTION"] == "The best Company"
