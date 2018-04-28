# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length = 120)
    image = models.ImageField(upload_to=upload_location, 
                                null=True, 
                                blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    new_field = models.CharField(max_length=140, default='DEFAULT VALUE')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    def update_content(self):
        return reverse("posts:update", kwargs={"id": self.id})

    def create_content(self):
        return reverse("posts:create")

    class Meta:
        ordering = ["-timestamp", "-updated"]