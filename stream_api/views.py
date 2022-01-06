from .models import *
from .serializers import StreamSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
import cv2
import subprocess
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

            stream_id=self.request.data['stream_id']

            content = []

            

            print("main_image_url:::::",stream_id)
           
            self.stream_function(stream_id)
           

            # add result to the dictionary and revert as response
            mydict = {
                'status': True,
                'response':
                    {

                        'Description':"Started Successfully",
                    }
            }
            content.append(mydict)

            return Response(content, status=status.HTTP_200_OK)
        errors = serializer.errors

        response_text = {
                "status": False,
                "response": errors
            }
        return Response(response_text, status=status.HTTP_400_BAD_REQUEST)
    def stream_function(self,stream_id):

        print("running stream started")
        rtmp = r'rtmp://35.154.58.17/live/output'
        # Read video and get attributes
        cap = cv2.VideoCapture("rtmp://35.154.58.17/live/nodeskwela")
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        sizeStr = str(size[0]) + 'x' + str(size[1])
        command = ['ffmpeg',
        '-y', '-an',
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', sizeStr,
        '-r', '25',
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        rtmp]
        pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE
        )
        font = cv2.FONT_HERSHEY_SIMPLEX

        # org
        org = (0, 50)
        # org1 = (0, 100)
        # org2 = (0, 150)

        # fontScale
        fontScale = 1

        # Blue color in BGR
        color = (255, 0, 0)

        # Line thickness of 2 px
        thickness = 1
        while cap.isOpened():
            success, frame = cap.read()
            frame = cv2.flip(frame,1)

            frame = cv2.putText(frame, 'Taking input from react  ', org, font, 
                            fontScale, color, thickness, cv2.LINE_AA)
            #     frame = cv2.putText(frame, 'native android camera ', org1, font, 
            #                    fontScale, color, thickness, cv2.LINE_AA)
            #     frame = cv2.putText(frame, 'processing through python OpenCV', org2, font, 
            #                    fontScale, color, thickness, cv2.LINE_AA)

            if success:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                pipe.stdin.write(frame.tostring())
            cap.release()
            pipe.terminate()
            