import face_recognition
import os
import cv2
from pickle import dump
KNOWN_FACES_DIR = '/home/pi/Desktop/KNOWN_FACES'

def main():
    def name_to_color(name):
        
        color = [(ord(c.lower())-97)*8 for c in name[:3]]
        return color


    print('Loading known faces...')
    known_faces = []
    known_names = []

    l = os.listdir(KNOWN_FACES_DIR)
    l.sort()
    for name in l:
        print('name - {}'.format(name))
        
        for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
            print('filename - {}'.format(filename))
            image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

            encoding = face_recognition.face_encodings(image)[0]

            # Append encodings and name
            known_faces.append(encoding)
            known_names.append(name)
            print(known_names,known_faces)
    return known_faces,known_names

known_faces,known_names = main()
f = open('face_encodings','wb')
g = open('names','wb')
dump(known_faces,f)
dump(known_names,g)
f.close()
g.close()
