from django.urls import path
from django.views.generic import TemplateView
from content_settings.views import FetchSettingsView, gen_hastag

from .models import Artist


urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="songs/index.html",
            extra_context={"artists": Artist.objects.all()},
        ),
        name="index",
    ),
    path("fetch/main/", FetchSettingsView.as_view(names=gen_hastag("main"))),
]
