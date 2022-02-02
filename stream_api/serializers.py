from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class StreamSerializer(serializers.Serializer):
    image=Base64ImageField(required=False) # From DRF Extra Fields
    
    
   

