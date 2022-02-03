from rest_framework import serializers



class StreamSerializer(serializers.Serializer):
    serializers=serializers.CharField(max_length=100000000000)
    
    
   

