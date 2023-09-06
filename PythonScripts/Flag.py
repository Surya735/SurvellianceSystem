from notify_run import Notify

def _raise(flag):
    notify = Notify()
    notify.send("Flag raised! - {}".format(flag))
    
with open('/home/pi/Desktop/alert.txt','r') as f:
    flag = f.readlines()[0]
    _raise(flag)                       

