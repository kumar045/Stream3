from .models import *
from .serializers import StreamSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .night_images import convert
import cv2
from PIL import Image
import base64
import numpy as np
import io
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

            stream_bytes=self.request.data['stream_bytes']
            stream_bytes = stream_bytes.split('base64,', 1 )[1]
           
            # print(stream_bytes)

            content = []

            

            # print("main_image_url:::::",stream_bytes)
           
            streambytes=self.stream_function(stream_bytes)
           

            # add result to the dictionary and revert as response
            mydict = {
                'status': True,
                'response':
                    {

                        'streambytes':streambytes,
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
    def stream_function(self,stream_bytes):
    #    print(stream_bytes)
       base64_img_bytes = stream_bytes.encode('utf-8')
       with open('decoded_image.png', 'wb') as file_to_save:
            decoded_image_data = base64.decodebytes(base64_img_bytes)
            file_to_save.write(decoded_image_data)
       image=cv2.imread("decoded_image.png")
       image=convert(image) 
       
    #    cv2.imwrite("image1.jpg",image)
       retval, buffer = cv2.imencode('.jpg', image)
       jpg_as_text = base64.b64encode(buffer)    

       return  jpg_as_text