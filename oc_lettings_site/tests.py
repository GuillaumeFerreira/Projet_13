import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_index_old():
    url = reverse("index_old")
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome to Holiday Homes" in response.content
