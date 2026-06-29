from django.urls import path
from .views import scene_view

urlpatterns = [
    path("", scene_view, name="start"),
    path("<str:scene_key>/", scene_view, name="scene"),
]