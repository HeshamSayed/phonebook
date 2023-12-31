from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from ..models.contact_model import Contact


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'
