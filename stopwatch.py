import time

nano = 00
s = 00
m = 00
h = 00

while True :
    nano += 1
    if nano >= 100 :
        nano = 0
        s += 1
    if s >= 60 :
        m += 1
        s = 0
    if m >= 60 :
        h += 1
        m = 0
    print(h, ":", m, ":", s, ".", nano)
    time.sleep(0.01)
