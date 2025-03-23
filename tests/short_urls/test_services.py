from short_urls.services import get_url_from_alias
from django.test.utils import override_settings

class TestGetShortURLFromAlias:
    MOCKED_DOMAIN_NAME = "example.com"

    @override_settings(DOMAIN_NAME=MOCKED_DOMAIN_NAME)
    def test_util_return_full_url_from_alias(self):
        alias = "xyz"

        assert get_url_from_alias(alias) == f"https://{self.MOCKED_DOMAIN_NAME}/{alias}"
