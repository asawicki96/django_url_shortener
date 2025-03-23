from short_urls.utils import generate_snowflake_id
from short_urls.models import ShortURL
import base62
from django.conf import settings


def get_or_create_short_url(long_url: str) -> ShortURL:
    if alias := ShortURL.objects.filter(long_url=long_url).first():
        return alias
    
    return create_short_url(long_url)

def create_short_url(long_url: str) -> ShortURL:
    return ShortURL.objects.create(
        alias=get_short_url_alias(),
        long_url=long_url
    )

def get_short_url_alias() -> str:
    # We use snowflake ID generator for scalability
    return base62.encode(generate_snowflake_id())

def get_url_from_alias(alias: str) -> str:
    return f"{settings.SCHEME}{settings.DOMAIN_NAME}/{alias}"