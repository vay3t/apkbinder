#!/usr/bin/python

import os

pwd=os.getcwd()
print "Press 'enter' to install requirements "
raw_input()
os.system("apt-get update && apt-get install dex2jar apktool")
os.system("rm /usr/share/apktool/apktool.jar")
os.system("cd /usr/share/apktool/ && wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.0.0.jar")
os.system("cd /usr/share/apktool/ && mv apktool_2.0.0.jar apktool.jar")
"""
binary=open("apkbinder","w")
binary.write("#!/bin/bash\n")
binary.write("")
binary.write('cd '+pwd+' && ./apkbinder.py "$@"')
binary.close()
os.system("chmod +x apkbinder")
os.system("mv -f apkbinder /usr/bin/apkbinder")
"""
print "[*] requirements installed"
