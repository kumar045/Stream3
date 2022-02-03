from rest_framework import serializers



class StreamSerializer(serializers.Serializer):
    stream_bytes=serializers.CharField(max_length=100000000000)
    
    
   

