from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(null=True)
    slug = models.SlugField(null=True)
    description = models.CharField(max_length=1000, blank=True)
    avg_rating = models.FloatField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre',blank=True,)
    def __str__(self):
        return f"{self.name} ({self.year})"
    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"

class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField(null=True)
    slug = models.SlugField(null=True)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.birth_year})"
        
class Actor(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(null=True)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"
    