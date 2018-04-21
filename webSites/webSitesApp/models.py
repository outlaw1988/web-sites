from django.db import models
from django.urls import reverse


class Website(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey('WebsiteCategory', on_delete=models.SET_NULL, null=True)
    date_added = models.DateField(null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('website-detail', args=[str(self.id)])


class WebsiteCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    date_added = models.DateField(null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class WebPage(models.Model):
    website = models.ForeignKey('Website', on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=1000, unique=True)
    date_added = models.DateField(null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return self.url
