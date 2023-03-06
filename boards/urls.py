from django.urls import path, include
from . import views

app_name = "boards"

urlpatterns = [
    path("", views.BoardAPI.as_view(), name="board-list"),
    path("<int:pk>", views.BoardDetailAPI.as_view(), name="board-detail"),
    path("copy", views.BoardCopyAPI.as_view(), name="board-copy"),
]