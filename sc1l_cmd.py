import time
import os
import psutil

def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds) 
# converting seconds to hh:mm:ss 

print("made by sc1lwlral. for only non-commercial use.")
while True :
    text = input(">> ")
    
    if text == 'help' :
        print("help -- show this message\nexit -- end the code\nmkdir -- make folder\nbs -- show battery status\ninfo -- show credit\ngithub -- show github link")
    elif text == 'exit' :
        print("exit")
        exit()
    elif text == 'mkdir' :
        try :
            fild = input("folder name >> ")
            os.mkdir(fild)
        except FileNotFoundError :
            print("folder failed to make (FileNotFoundError)")
    elif text == 'bs' :
        battery = psutil.sensors_battery()
        print("Battery percentage : ", battery.percent,"%") 
        print("Power plugged in : ", battery.power_plugged) 
        print("Battery left : ", convertTime(battery.secsleft)) 
    elif text == 'hidden' :
        print("non-exist command?")
        time.sleep(1)
        print("you found hidden message!")
    elif text == 'info' :
        print("made by sc1lwlral\nused time os psutil")
    elif text == 'github' :
        os.system("github.com/sjchoi10000")
    else :
        print("non-exist command!")
