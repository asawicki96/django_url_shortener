from rest_framework.generics import CreateAPIView, RetrieveAPIView
from short_urls.serializers import ShortURLCreateSerializer, ShortURLRetrieveSerializer
from short_urls.services import get_or_create_short_url
from short_urls.models import ShortURL

class CreateShortURLView(CreateAPIView):
    serializer_class = ShortURLCreateSerializer

    def perform_create(self, serializer: ShortURLCreateSerializer):
        serializer.instance = get_or_create_short_url(
            long_url=serializer.validated_data["long_url"]
        )

class RetrieveShortURLView(RetrieveAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLRetrieveSerializer
    lookup_field = "alias"


    
        