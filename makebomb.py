dummynum = 0
ddummy = 0

print("DONT RUN IN HOST COMPUTER! ( RUN : R  , EXIT : X )")
gab = input("WRITE HERE : ")
if gab == "x" :
    exit()
if gab == "X" :
    exit()
        
while True :
    f = open(ddummy, 'a')
    f.write("makebomb")
    print(dummynum, "makebomb spawned")
    dummynum += 1
    ddummy = str(dummynum)