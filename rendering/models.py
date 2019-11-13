from django.db import models

# Create your models here.
class Rendering(models.Model):
        description = models.CharField(max_length=255, blank=True)
        document = models.FileField(upload_to='img')

def _str_(self):
    return self.name