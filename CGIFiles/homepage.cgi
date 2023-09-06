
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#enable debugging
import cgitb

with open('/home/pi/Desktop/IP','r') as f:
    ip = f.read()

f = open('/home/pi/Desktop/Daily-report')
m = f.readlines()
l = []
for i in m:
    l.append(i.split(':')[1].split('\n')[0])
cgitb.enable()
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

print('.icon {')
print("    background-image: url('/Images/logo.png');")
print("    height: 63px;")
print("    width: 60px;")
print("    display: block;")
print("}")


print("</style>")
print("</head>")

print("<div class='sidenav'>")
print("  <a style='font-size:35px'><span class = 'icon' align = 'center'></span>Kronos</a>")
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
print('<body text = "white">')
print('<h3 align = "center" style="font-size: 40px;">')
# print("<br>")
# print('<br>')
# print('<br>')
# print('<br>')
print('<br>')
print('<br>')


print("<br>")
print("Daily Report")
print("</h3>")
print('<table width="600" border="10" align="center" cellpadding="6" cellspacing="6" bordercolor="#dddddd"  style="border-style:hidden"  >')
print("  <tbody  >")
# print("    <tr>")
# print("      <td>No. of people seen:</td>")
# print("      <td>{}</td>".format(l[0]))
# print("    </tr>")
print("    <tr>")
print("      <td>No. of sightings:</td>")
print("      <td>{}</td>".format(l[1]))
print("    </tr>")
print("    <tr>")
print("      <td>No. recognized:</td>")
print("      <td>{}</td>".format(l[2]))
print("    </tr>")
print("    <tr>")
print("      <td>No. of unknowns:</td>")
print("      <td>{}</td>".format(l[3]))
print("    </tr>")
print("    <tr>")
print("      <td>Last movement:</td>")
print("      <td>{}</td>".format(l[4]))
print("    </tr>")
print("  </tbody>")
print("</table>")
print("</body>")
print("</html>")
