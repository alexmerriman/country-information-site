from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Area(models.Model):
    name = models.CharField(max_length=100)
    area_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.area_type})"

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name="attractions"
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="attractions/", blank=True, null=True)

    def __str__(self):
        return self.name