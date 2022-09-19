from django.urls import reverse
from django.test import Client
import pytest
from .models import Profile
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_profiles_index():
    url = reverse("profiles_index")
    client = Client()
    response = client.get(url)
    assert response.status_code == 200

    assert b"Profiles" in response.content

@pytest.mark.django_db
def test_profile():
    user_test = User.objects.create_user(username="test", password="156481215", first_name="",last_name="")
    profile = Profile.objects.create(user=user_test, favorite_city="")
    client = Client()
    url = reverse("profile", kwargs={"username": "test"})
    response = client.get(url)
    assert response.status_code == 200
    assert profile.user.username in response.content.decode()
