print("="*5,"sc1l's cmd","="*5)
print()

try:
    import psutil
except:
    print('failed to load psutil. did you downloaded psutil?')
    exit()
try:
    import os
except:
    print('failed to load os. did you downloaded os?')
    exit()

def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def showtask():
    processes = psutil.process_iter()
    for process in processes:
        print(f"Process ID: {process.pid}, Name: {process.name()}")

print('type help for commands. press ctrl + c to exit when you got stuck.')
while True:
    cmd = input('>> ')
    if cmd == "task":
        check = input('this command shows all of process of your os. do you wanna continue?(Y/N) ')
        if check == "Y" or check == "y":
            showtask()
    elif cmd == "help":
        print(''' * all commands only tested on windows! this script can be unstable on other os
help - show this screen.
task - shows all tasks on your os.
exit - exit this script.
cmd - runs command in your os. (works with linux)
batteryinfo - shows battery info
folder - make folder in this folder.
convsec - convert second to Hour, Minutes, Seconds.''')
    elif cmd == "exit":
        print("closing script...")
        exit()
    elif cmd == "cmd":
        print("type command to excute")
        temp1 = input(">> ")
        os.system(temp1)
    elif cmd == "batteryinfo":
        battery = psutil.sensors_battery()
        print("Battery percentage : ", battery.percent,"%")
        print("Power plugged in : ", battery.power_plugged)
        print("Battery left : ", convertTime(battery.secsleft))
    elif cmd == "folder":
        print('folder name')
        folder = input('>> ')
        try :
            os.mkdir(folder)
        except :
            print('failed to make folder.')
    elif cmd == "convsec":
        print('type time (seconds)')
        try:
            tim = int(input('>> '))
            print(convertTime(tim))
        except :
            print('failed to convert time.')
    else:
        if cmd != "":
            print(cmd,"- not exist command")
