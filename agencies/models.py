from django.db import models

class Agency(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
