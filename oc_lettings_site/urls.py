from django.contrib import admin
from django.urls import path
from profiles.views import profile, profiles_index
from lettings.views import index, letting
from .views import index_old, trigger_error


urlpatterns = [
    path("", index_old, name="index_old"),
    path("lettings/", index, name="index"),
    path("lettings/<int:letting_id>/", letting, name="letting"),
    path("profiles/", profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", profile, name="profile"),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
