from django.views.generic.list import ListView
from ..models.contact_model import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'
