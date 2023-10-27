from django.conf import settings
from django.db import models


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(verbose_name="Firstname", max_length=100)
    lastname = models.CharField(verbose_name="Lastname", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
