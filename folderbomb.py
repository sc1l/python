import os
#os 모듈 임포트

mkdirnum = 0
#mkdirnum 변수 생성

while True :
    os.mkdir(str(mkdirnum)+" dummy folder")
    print(mkdirnum, "dummy folder spawned")
    mkdirnum += 1