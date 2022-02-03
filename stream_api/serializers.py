from rest_framework import serializers
from base64.fields import Base64ImageField


class StreamSerializer(serializers.Serializer):
    stream_bytes= Base64ImageField(required=False)

    
    
   

