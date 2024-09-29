from django.urls import path
from django.views.generic import TemplateView, ListView

from .models import Book
from content_settings.views import (
    FetchSettingsView,
)


class BookListView(ListView):
    model = Book
    template_name = "books/list.html"


app_name = "books"
urlpatterns = [
    path("", TemplateView.as_view(template_name="books/index.html"), name="index"),
    path(
        "fetch/main/",
        FetchSettingsView.as_view(
            names=[
                "RATINGS",
                "COMPANY_DESCRIPTION",
            ]
        ),
        name="fetch_main",
    ),
]
