from django.urls import path
from .views import receive_message

urlpatterns = [
    path('receive_message/', receive_message, name='receive_message'),
]




