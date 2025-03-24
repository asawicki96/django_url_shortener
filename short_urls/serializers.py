from rest_framework import serializers
from short_urls.models import ShortURL
from short_urls.services import get_url_from_alias

class ShortURLCreateSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ("short_url", "long_url", "alias")
        read_only_fields = ("alias",)

    def get_short_url(self, obj: ShortURL) -> str:
        return get_url_from_alias(obj.alias)
    

class ShortURLRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ("long_url",)