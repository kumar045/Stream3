from .models import *
from .serializers import StreamSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
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
        stream_bytes=self.request.data['name']
        print(stream_bytes)

        if serializer.is_valid():

            stream_bytes=self.request.data['name']
            stream_bytes="file://storage/emulated/0/Pictures/"+str(stream_bytes)
           
            print(stream_bytes)

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
            print(content)

            return Response(content, status=status.HTTP_200_OK)
        errors = serializer.errors

        response_text = {
                "status": False,
                "response": errors
            }
        return Response(response_text, status=status.HTTP_400_BAD_REQUEST)
    def stream_function(self,stream_bytes):
        print(stream_bytes)

        image = Image.open(stream_bytes)
        image_np = np.array(image)
        image = cv2.putText(image_np, 'OpenCV', (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        # cv2.imwrite("image1.jpg",image)
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        # # decodeit = open('image3.jpg', 'wb')
        # # decodeit.write(base64.b64decode((jpg_as_text)))
        # # decodeit.close()             
        # # print(image_np)
        return jpg_as_text