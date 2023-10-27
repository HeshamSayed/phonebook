from django.urls import path

from .views.add_contact_view import AddContactView
from .views.contact_list_view import ContactListView
from .views.contact_detail_view import ContactDetailView

urlpatterns = [
    path('add/', AddContactView.as_view(), name='add_contact'),
    path('list/', ContactListView.as_view(), name='contact_list'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),

]
