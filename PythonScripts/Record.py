from os import system
from datetime import datetime
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from PIL import Image

camera = PiCamera()
camera.resolution = (480, 480)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(480, 480))

def capture():
    time.sleep(1)
    i = 1
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    system('sudo mkdir /home/pi/Desktop/frames/{}'.format(current_time))
    system('sudo chmod a=rwxX /home/pi/Desktop/frames/{}'.format(current_time))

    for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
        if i == 75:
            camera.close()
            break
        else:
            
            image = frame.array

            im = Image.fromarray(image)
            im.save("/home/pi/Desktop/frames/{0}/frame{1}.jpg".format(current_time,i))

            
            i+=1
            
            rawCapture.truncate(0)
            rawCapture.seek(0)
#         if process(rawCapture):
#             break

    return current_time
current_time = main()
print('done')
system('python3 /home/pi/Desktop/recog.py')
