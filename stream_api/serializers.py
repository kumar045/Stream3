from rest_framework import serializers


class StreamSerializer(serializers.Serializer):
    stream_id = serializers.CharField()
    

