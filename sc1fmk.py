#TMI : 파일 다시만듬

print("need bs4 and os")
from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
#load modules

print("Python file loaded")

if os.path.isdir("sc1fmk") == False :
    os.mkdir("sc1fmk")
#make sc1fmk

gitlink = urlopen("https://raw.githubusercontent.com/sjchoi10000/python/main/files")
select = BeautifulSoup(gitlink.read(), "html.parser")
url = input(select)
#make input py file

reset = open("sc1fmk/"+url+"from github.py", 'w')
reset.write("")
#reset .py file

f = open("sc1fmk/"+url+" from github.py", 'w')
#open .py

giturl = urlopen("https://raw.githubusercontent.com/sjchoi10000/python/main/"+url+".py")
#save url as giturl

raw = BeautifulSoup(giturl.read(), "html.parser")
#make raw

f.write(str(raw))
f.close
#write raw

print("downloaded")
yn = input("you want to view source? (Y/N)")
if yn == "y" :
    print(raw)
if yn == "Y" :
    print(raw)
