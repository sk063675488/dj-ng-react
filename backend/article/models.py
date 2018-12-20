from django.db import models

# Create your models here.
class article_model(models.Model):
    name = models.CharField(max_length = 200)
    content = models.CharField(max_length = 300)
    descs = models.TextField()

    def __str__(self):
        return (self.name)