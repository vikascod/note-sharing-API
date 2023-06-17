from django.db import models

# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=100)
    files = models.FileField(upload_to='notes')

    def __str__(self):
        return self.name