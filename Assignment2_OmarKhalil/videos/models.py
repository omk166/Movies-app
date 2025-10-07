from django.db import models

class Video(models.Model):
    GENRES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Other', 'Other'),
    ]

    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=100)
    Actor2Name = models.CharField(max_length=100, blank=True, null=True)
    DirectorName = models.CharField(max_length=100)
    MovieGenre = models.CharField(max_length=50, choices=GENRES)
    ReleaseYear = models.IntegerField()

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
