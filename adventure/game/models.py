from django.db import models

class Scene(models.Model):
    key = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    is_ending = models.BooleanField(default=False)

    def __str__(self):
        return self.key


class Choice(models.Model):
    scene = models.ForeignKey(Scene, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    next_scene = models.ForeignKey(
        Scene,
        related_name="next_scenes",
        on_delete=models.CASCADE,
        null=True,       # TEMPORARY
        blank=True
    )
    
    def __str__(self):
        return f"{self.text} → {self.next_scene.key}"