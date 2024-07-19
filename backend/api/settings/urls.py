from django.urls import path

from . import currency, change_name, profile_picture
from .api_keys import generate_api_key_endpoint, revoke_api_key_endpoint
from .defaults import handle_client_defaults_endpoints

urlpatterns = [
    path(
        "change_currency/",
        currency.update_currency_view,
        name="change_currency",
    ),
    path(
        "change_name/",
        change_name.change_account_name,
        name="change_name",
    ),
    path("profile_picture/", profile_picture.change_profile_picture_endpoint, name="update profile picture"),
    path("api_keys/generate/", generate_api_key_endpoint, name="api_keys generate"),
    path("api_keys/revoke/<str:key_id>/", revoke_api_key_endpoint, name="api_keys revoke"),
    path("client_defaults/<int:client_id>/", handle_client_defaults_endpoints, name="client_defaults"),
    path("client_defaults/", handle_client_defaults_endpoints, name="client_defaults without client"),
]

app_name = "settings"
