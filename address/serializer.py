# ModelSerializer is a layer of abstraction over the default serializer that allows to 
# quickly create a serializer for a model in Django. Django REST Framework is a 
# wrapper over default Django Framework, basically used to create APIs of various kinds. 
# There are three stages before creating a API through REST framework, 
# Converting a Model’s data to JSON/XML format (Serialization), 
# Rendering this data to the view, Creating a URL for mapping to the viewset.


from rest_framework.serializers import ModelSerializer
from .models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
