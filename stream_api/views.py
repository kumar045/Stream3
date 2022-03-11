from .models import *
from .serializers import StreamSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
import numpy as np
import io
from transformers import pipeline
class StreamAPIView(CreateAPIView):
    serializer_class =StreamSerializer
    queryset = Stream.objects.all()
    def create(self, request, format=None):
        """
                Takes the request from the post and then processes the algorithm to extract the data and return the result in a
                JSON format
                :param request:
                :param format:
                :return:
                """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            stream_text=self.request.data['stream_text']
            
           
            # print(stream_bytes)

            content = []

            

            # print("main_image_url:::::",stream_bytes)
           
            streamtext=self.stream_function(stream_text)
           

            # add result to the dictionary and revert as response
            mydict = {
                'status': True,
                'response':
                    {

                        'streamtext':streamtext,
                    }
            }
            content.append(mydict)
            # print(content)

            return Response(content, status=status.HTTP_200_OK)
        errors = serializer.errors

        response_text = {
                "status": False,
                "response": errors
            }
        return Response(response_text, status=status.HTTP_400_BAD_REQUEST)
    def stream_function(self,stream_text):

        
 
 
        mysummarization = pipeline("summarization")
        
        
        
        # Get the Summary
        mysummary = mysummarization(stream_text)
        
        text=mysummary[0]['summary_text']
    

        return  text