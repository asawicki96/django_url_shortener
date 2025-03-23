from rest_framework.routers import path
from short_urls.views import CreateShortURLView, RetrieveShortURLView
app_name = "short_urls"

urlpatterns = [
    path("", CreateShortURLView.as_view(), name="create_short_url"),
    path("<str:domain>/<str:alias>", RetrieveShortURLView.as_view(), name="retrieve_short_url")
]