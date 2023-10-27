from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ..models.contact_model import Contact


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'
