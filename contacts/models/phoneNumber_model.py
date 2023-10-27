from django.db import models

from .contact_model import Contact


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    mobile_phone = models.CharField(verbose_name="Mobile phone", max_length=100)

    def __str__(self):
        return str(self.contact) + " mobile number is " + str(self.mobile_phone)
