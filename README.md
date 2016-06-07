# apkbinder
Automatic backdooring apk with meterpreter (PoC)

# How to
apk place within "apkbinder" directory, named app-debug.apk

# Dependencies
```
Kali-Rolling:
	python 2.7.x libraries: os re shutil zipfile tempfile argparse
	metasploit
	apktool 2.0
	dex2jar
```
	
# Components
```
apkbinder.py - APK automatic backdooring script
permisos.xml - Permission of meterpreter
list_apk.txt - dependence of mass-trojanizer module

```

# Command line
```
usage: apkbinder.py [-h] -l LHOST [-p LPORT] [-m]

Backdooring APK with meterpreter

optional arguments:
  -h, --help            show this help message and exit
  -l LHOST, --lhost LHOST
                        LHOST select local host
  -p LPORT, --lport LPORT
                        LPORT select local port
  -m, --mas-trojanizer  Massive trojanization module, you need edit file:
                        list_apk.txt
```

# Modules
- mass-trojanizer -> module for massive trojanization, need list of ubications apk in list_apk.txt

# Comments
script based by https://github.com/nodoraiz/AndroidAnalysis/blob/master/modify.py (nodoraiz)

# Bugs
create multiple sessions, but only one has privileges

# Authors
vay3t & 4c1d0_b1n4r10

# Copying
###### Copyright 2015-2016 (C) Vay3t <https://twitter.com/vay3t>
###### License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
