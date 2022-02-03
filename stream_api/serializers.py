from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class StreamSerializer(serializers.Serializer):
    stream_bytes=Base64ImageField() # From DRF Extra Fields
   

    
    
   

