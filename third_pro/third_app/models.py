from django.db import models

# Create your models here.


class UserPage(models.Model):
    frst_name = models.CharField(max_length=264, unique=True)
    last_name = models.CharField(max_length=264, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.frst_name


