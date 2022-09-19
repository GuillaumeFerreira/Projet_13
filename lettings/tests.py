from django.urls import reverse
from django.test import Client
import pytest
from .models import Address, Letting


@pytest.mark.django_db
def test_index():
    url = reverse("index")
    client = Client()
    response = client.get(url)
    assert response.status_code == 200

    assert b"Lettings" in response.content


@pytest.mark.django_db
def test_letting():
    client = Client()
    url = reverse("letting", kwargs={"letting_id": 1})
    response = client.get(url)
    assert response.status_code == 200
