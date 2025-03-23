import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from short_urls.models import ShortURL
from short_urls.services import get_url_from_alias

class TestCreateShortURLView:
    @pytest.fixture
    def view_url(self) -> str:
        return reverse("short_urls:create_short_url")
    
    def test_view_response_data(self, view_url: str, client: APIClient, example_url: str):
        payload = {"long_url": example_url}

        response = client.post(path=view_url, data=payload)

        short_url = ShortURL.objects.filter(long_url=payload["long_url"]).first()

        assert response.status_code == status.HTTP_201_CREATED
        assert short_url
        assert response.data == {
            "short_url": get_url_from_alias(short_url.alias),
            "alias": short_url.alias,
            "long_url": payload["long_url"]
        }

    def test_view_return_existing_short_url(self, view_url: str, client: APIClient, example_url: str):
        existing_short_url = ShortURL.objects.create(long_url=example_url, alias="xyz")

        payload = {"long_url": existing_short_url.long_url}
        response = client.post(path=view_url, data=payload)

        assert ShortURL.objects.count() == 1
        assert response.data.get("alias") == existing_short_url.alias


class TestUrlRetrieveShortURLView:
    def get_view_url(self, domain: str, alias: str) -> str:
        return reverse("short_urls:retrieve_short_url", kwargs={"domain": domain, "alias": alias})
    
    def test_view_response_data(self, client: APIClient, example_url: str, settings):
        existing_short_url = ShortURL.objects.create(long_url=example_url, alias="xyz")
        
        response = client.get(path=self.get_view_url(domain=settings.DOMAIN_NAME, alias=existing_short_url.alias))

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "long_url": existing_short_url.long_url
        }
