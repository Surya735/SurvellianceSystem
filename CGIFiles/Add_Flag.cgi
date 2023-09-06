
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#enable debugging

import cgi,cgitb

cgitb.enable()

form = cgi.FieldStorage()
name = form.getvalue('name')
f = open('/home/pi/Desktop/Flags.txt','a')
f.write(name)
f.close()

with open('/home/pi/Desktop/IP','r') as f:
    ip = f.read()


print("Content-Type: text/html;charset=utf-8");
print()
print("<html>")
print("<head>")
print("<meta charset='utf-8'>")
print("<title>Kronos</title>")
print('<style type="text/css">')

print("body {")
print(" font-family: courier new;")    
print(" background-image: url('/Images/Dark-Navy-Blue-Wallpaper.png');")
print(" background-size:100%")
    
print("}")

print(".sidenav {")
print("  height: 100%;")
print('  width: 200px;')
print('  position: fixed;')
print('  z-index: 1;')
print('  top: 0; ')
print('  left: 0;')
print('  background-color: #111;')
print('  overflow-x: hidden;')
print('  padding-top: 20px;')
print('}')


print('.sidenav a {')
print('  padding: 6px 8px 6px 16px;')
print('  text-decoration: none;')
print('  font-size: 25px;')
print('  color: #818181;')
print('  display: block;')
print('}')

print('.sidenav a:hover {')
print('  color: #f1f1f1;')
print('}')

print('.main {')
print('  margin-left: 160px;')
print('  padding: 0px 10px;')
print('}')

print('.input_box')
print('{')
print('    height:200px;')
print('    font-size:14pt;')
print('}')

print('.icon {')
print("    background-image: url('/Images/logo.png');")
print("    height: 63px;")
print("    width: 60px;")
print("    display: block;")
print("}")


print("</style>")
print("</head>")
print("<div class='sidenav'>")
print("  <a style='font-size:35px'><span class = 'icon'></span>Kronos</a>")
print("  <a></a>")
print("  <a></a>")
print("  <a class='active' href='http://{}/cgi-bin/homepage.cgi'>Home</a>".format(ip))
print('  <a href="http://{}/cgi-bin/search.cgi">Search</a>'.format(ip))
print('  <a href="http://{}/cgi-bin/Flag_form.cgi">Flag</a>'.format(ip))
#   <div class="topnav-right">
#     <a href="#search">Search</a>
#     <a href="#about">About</a>
#   </div>
print(" </div>")


