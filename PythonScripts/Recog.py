import face_recognition
import os
import cv2
from pickle import load
from PIL import Image

KNOWN_FACES_DIR = '/home/pi/Desktop/KNOWN_FACES'
UNPROCESSED_FACES_DIR = '/home/pi/Desktop/frames' 
TOLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model
flag = False

# Returns (R, G, B) from name
with open('/home/pi/Desktop/Flags.txt','r') as f:
    flags = f.readlines()
    print(flags)
def name_to_color(name):
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color


print('Loading known faces...')
f = open('face_encodings','rb')
g = open('names','rb')
known_faces=load(f)
known_names=load(g)
f.close()
g.close()
# print(known_faces)
match_ct = 0
print('Processing unknown faces...')

for directory in os.listdir(UNPROCESSED_FACES_DIR):
    ct=1
    empty_capture = True
    os.system('sudo mkdir /home/pi/Desktop/Frames/{}'.format(directory))
    os.system('sudo chmod a=rwxX /home/pi/Desktop/Frames/{}'.format(directory))  
    t = os.listdir('/home/pi/Desktop/frames/{}'.format(directory))
    l = []
    for i in t:
        s = ''
        for j in i:
            if j.isdigit():
                s+=j
        l.append(int(s))
    l.sort()
    print(l)
    for i in l:
        matches = []
        image = face_recognition.load_image_file(f'{UNPROCESSED_FACES_DIR}/{directory}/frame{i}.jpg')

        # This time we first grab face locations - we'll need them to draw boxes
        locations = face_recognition.face_locations(image, model=MODEL)

        # Now since we know loctions, we can pass them to face_encodings as second argument
        # Without that it will search for faces once again slowing down whole process
        encodings = face_recognition.face_encodings(image, locations)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
        print(f' Found {len(encodings)} face(s)')
        if len(encodings)>0:
            empty_capture = False
        
        for face_encoding, face_location in zip(encodings, locations):
            unknown = True
            for i in range(len(known_faces)):
                
                results = face_recognition.compare_faces(known_faces[i],[face_encoding], TOLERANCE)
                
                # Since order is being preserved, we check if any face was found then grab index
                # then label (name) of first matching known face withing a tolerance
                match = None
                print(results)
                #print(known_names)
                if True in results:  # If at least one is true, get a name of first of found labels
                    match = known_names[i]
                    print(f' - {match} from {results}')
                    matches.append(match)
                    if match in flags:
                        with open('/home/pi/Desktop/alert.txt','w') as f:
                            f.write(f' {match}')                       
                            flag = True
                    unknown = False
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    color = name_to_color(match)

                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)


                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                    if not unknown:
                        cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)
                    elif unknown:
                        cv2.putText(image, 'Unknown', (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)
                
                    match_ct+=1
                    ct+=1
                    match_str =''                         
                    for m in matches:
                        match_str+=m
                    im = Image.fromarray(image)
                    im.save("/home/pi/Desktop/Frames/{0}/{1}{2}.jpg".format(directory,match_str,ct))
                                
#                 else:
#                     im = Image.fromarray(image)
    os.system('sudo rm -r /home/pi/Desktop/frames/{}'.format(directory))
    if empty_capture:
        os.system('sudo rm -r /home/pi/Desktop/Frames/{}'.format(directory))
        os.system('sudo rmdir /home/pi/Desktop/Frames/{}'.format(directory))
    if flag:
        os.system('python3 /home/pi/Desktop/Flag.py')

