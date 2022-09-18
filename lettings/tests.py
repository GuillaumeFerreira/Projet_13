from django.urls import reverse
from django.test import Client
import pytest


@pytest.mark.django_db
def test_index():
    url = reverse('index')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200

    assert b"Lettings" in response.content

def test_letting():
    assert 1