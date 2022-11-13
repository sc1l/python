#TMI : 파일 다시만듬

from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
#load modules

if os.path.isdir("sc1fmk") == False :
    os.mkdir("sc1fmk")
#make sc1fmk

url = input("makebomb or hack or filebomb or Luck : ")
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