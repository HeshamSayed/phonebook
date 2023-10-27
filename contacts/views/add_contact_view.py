from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from ..forms.forms import ContactForm, PhoneNumberFormSet


class AddContactView(LoginRequiredMixin, View):
    template_name = 'add_contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        formset = PhoneNumberFormSet()
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        formset = PhoneNumberFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user  # Assuming you have a logged-in user
            contact.save()
            formset.instance = contact
            formset.save()
            return redirect('contact_list')
        return render(request, self.template_name, {'form': form, 'formset': formset})
