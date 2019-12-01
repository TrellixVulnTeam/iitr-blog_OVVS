from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to=None, blank=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
