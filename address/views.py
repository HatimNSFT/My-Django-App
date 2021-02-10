from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Address
from .serializer import AddressSerializer
# Create your views here.

# 'Serializers'
# They're used to convert the data sent in a HTTP request to a Django object 
# and a Django object to a valid response data.

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer    # Instance of Manager which has a interface through
    queryset = Address.objects.all()        # which DB query operations are provided.
