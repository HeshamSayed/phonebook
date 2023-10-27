from django import forms

from ..models.contact_model import Contact
from ..models.phoneNumber_model import PhoneNumber


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['mobile_phone']


PhoneNumberFormSet = forms.inlineformset_factory(
    Contact, PhoneNumber, form=PhoneNumberForm, extra=1
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email']
