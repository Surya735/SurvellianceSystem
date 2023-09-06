
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#enable debugging
from os import system,listdir
import cv2
import numpy as np
import glob
import cgi, cgitb
from PIL import Image
form = cgi.FieldStorage()
name = form.getvalue('name')
results = {}

with open('/home/pi/Desktop/IP','r') as f:
    ip = f.read()
    


for directory in listdir('/home/pi/Desktop/Frames'):
    found = False
    t = listdir('/home/pi/Desktop/Frames/{}'.format(directory))
    d = {}
    filenames=[]    
    for i in t:
        
        if name in i:
            n = ''.join([j for j in i if not j.isdigit()])[:-4]
            k = ''.join([j for j in i if j.isdigit()])
            d[int(k)] = n
            found = True
        
    D =list(d.keys())
    D.sort()
    if D != None:
        for i in D:
            filenames.append(d[i] + str(i) + '.jpg')
    if found:
        results[directory] = filenames        
#print(results)
cgitb.enable()
print("Content-type:text/html;charset=utf-8")
print()
print()
print('<html>')
print()
print("<head>")
print("<meta charset='utf-8'>")
print("<title>Kronos</title>")
print('<style type="text/css">')
print("body {")
    
print(" background-image: url('/Images/Dark-Navy-Blue-Wallpaper.png');")
print(" background-size:100%")
    
print("}")
print("</style>")
print("</head>")

print("<body>")
if len(results)==0:
    print("   <h1>No records found</h1>")
else:
    print("   <center><h1 style='color:powderblue;font-family:courier new;'>Subject was spotted at:</h1></center>")
    print("<p>")

    for time in results:
        #print(time)
        system("sudo mkdir /home/pi/Desktop/temp/{}".format(time))
        system("sudo chmod a=rwxX /home/pi/Desktop/temp/{}".format(time))
        ct=1
        
        img, *imgs = [Image.open('/home/pi/Desktop/Frames/{0}/{1}'.format(time,f)) for f in results[time]]
        img.save('/home/pi/Desktop/temp/{}/{}'.format(time,time), format='GIF', append_images=imgs,save_all=True, duration=80, loop = 0)
        
        
for time in results:
    system("sudo cp /home/pi/Desktop/temp/{0}/{0} /var/www/Frames".format(time))

print('<center><Table border="1" cellspacing="0" width="350px" bordercolor="#FFFFFF" bgcolor = "grey">')
print('<td colspan="{}">'.format(len(results)))
print('<table border="2" width="100%">')

for time in results:
    
    print('    <tr><td width="50%"><center><a href = "http://{0}/Images/{1}">{1}</a></center></td></tr>'.format(ip,time))

    print("</p>")
print('</Table></center>')
print("</body>")
print("</html>")
#      sudo chmod a=rwxX /home/pi/Desktop/19:01:02
