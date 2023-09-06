from os import system,listdir
from subprocess import check_output
from time import sleep

unprocessed_frames_dir = '/home/pi/Desktop/frames'
try:
    status = str(check_output("ps -r", shell=True))
    if '/home/pi/Desktop/recog.py' in status:
        print('In status dont execute recog')
        l = len(listdir(unprocessed_frames_dir))
        if '/home/pi/Desktop/enqueue.py' not in status:
            while True:
                sleep(30)
                status = str(check_output("ps -r", shell=True))
                if '/home/pi/Desktop/recog.py' not in status:
                    print('Finished running previous execute recog')
                    system('lxterminal -e python3 /home/pi/Desktop/recog.py')
                    break
    else:
        print('Not in status')
    
except:
    print('Nothing running execute recog')
    system('lxterminal -e python3 /home/pi/Desktop/recog.py')

