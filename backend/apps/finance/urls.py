from django.urls import path

from apps.finance.views import (
    ContextListCreateView,
    ContextDetailView,
)


urlpatterns = [
    path(
        "contexts/",
        ContextListCreateView.as_view(),
        name="context-list-create",
    ),
    path(
        "contexts/<int:context_id>/",
        ContextDetailView.as_view(),
        name="context-detail",
    )
]
