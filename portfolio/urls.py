from django.urls import path

from . import views
from . import contact

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', contact.send, name='send'),
    path('contact/thanks/', contact.success, name='tks'),

]