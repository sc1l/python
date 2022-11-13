import time

s = 00
m = 00
h = 00

while True :
    s += 1
    if s >= 60 :
        m += 1
        s = 0
    if m >= 60 :
        h += 1
        m = 0
    print(s, "sec", m, "mintue", h, "hours")
    time.sleep(1.000000)