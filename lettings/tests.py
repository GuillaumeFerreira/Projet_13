from django.urls import reverse
from django.test import Client
import pytest
from .models import Address, Letting


@pytest.mark.django_db
def test_index_old():
    url = reverse("index_old")
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome to Holiday Homes" in response.content


@pytest.mark.django_db
def test_index():
    url = reverse("index")
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content


@pytest.mark.django_db
def test_letting():
    address = Address.objects.create(
        number=1, street="", city="", state="FR", zip_code=12, country_iso_code="125"
    )
    letting = Letting.objects.create(title="Jules Verne", address=address)
    client = Client()
    url = reverse("letting", kwargs={"letting_id": 1})
    response = client.get(url)
    assert response.status_code == 200
    assert letting.title in response.content.decode()
