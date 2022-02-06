from rest_framework import serializers



class StreamSerializer(serializers.Serializer):
    stream_bytes=serializers.ImageField() # From DRF Extra Fields
   

    
    
   

