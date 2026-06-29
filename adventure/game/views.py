from django.shortcuts import render, get_object_or_404
from .models import Scene

def scene_view(request, scene_key="forest_start"):
    scene = get_object_or_404(Scene, key=scene_key)

    return render(request, "game/scene.html", {
        "scene": scene
    })