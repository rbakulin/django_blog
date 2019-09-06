from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def snippet(self):
        return f'{self.body[:50]}...' if len(self.body) > 50 else self.body
