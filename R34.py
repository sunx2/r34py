#!/usr/bin/env python3
__author__="sun <SunSoftwares.pvt>"
__copyright__= "Sun(2016-17)" 
__license__="no"
__status__="Production"
__version__="1.0"
#Thanks for using it
from bs4 import BeautifulSoup as bs
import requests
import os,sys
import random
from random import randint
#styles 

class colors:
	bold='\033[1m'
	blue='\033[34m'
	green='\033[32m'
	red='\033[31m'
	magenta="\033[35m"
	white='\033[37m'
	#backgrounds
	bgwhite='\033[47m'
	normal='\033[2m'
	off='\033[0m'
	black='\033[30m'
	
	


#done
print(colors.bold
+colors.blue+' *****************************')
print(colors.magenta+" Welcome to "+colors.bgwhite+colors.red+"script Downloader \n"+colors.off)
print(colors.bold+colors.blue+" *****************************\n")
t1=input(colors.white+" Please enter tag :  "+colors.green)
t2=input(colors.white+"\n Please enter page no : "+colors.green)
url="http://rule34.paheal.net/post/list/"+t1+"/"+t2
print(colors.white+colors.normal+" configuring.....")
print(" sending http request...."+colors.black)
try:
	webpage=requests.get(url)
	
except:
	print(colors.bgwhite+colors.red+" Error !"+colors.off+colors.white+colors.bold+" No network connection found"+colors.off)
	exit()
	
htmls=webpage.text
print(colors.white+colors.normal+" connected .....")
print(" indexing images ......")
print(" \n \n")
payload=bs(htmls,'html.parser')
images=payload.find_all(string="Image Only")
try:
	if len(images)!=0:
		print(colors.off+colors.bold+colors.bgwhite+colors.blue+" Success !"+colors.off+colors.white+colors.bold+" Found "+colors.green+str(len(images))+colors.white+" Images"+colors.off)
except:
	print(colors.bgwhite+colors.red+" Error !"+colors.off+colors.white+colors.bold+" Wrong tag entered "+colors.off)
	exit()
#main work begins
print(" \n \n")
print(" Searching for Image formats...")
zero=0
imagetags=[]
imagelinks=[]
while zero<len(images):
	imagetags=imagetags+[images[zero].find_parent('a')]
	zero=zero+1
zero=0
while zero<len(images):
	for link in imagetags:
		imagelinks=imagelinks+[link.get("href")]
		zero=zero+1
jpg=[]
png=[]
others=[]
zero=0
while zero<len(imagelinks):
	if "jpg" in imagelinks[zero]:
		jpg=jpg+[imagelinks[zero]]
		zero=zero+1
	elif "png" in imagelinks[zero]:
		png=png+[imagelinks[zero]]
		zero=zero+1
	else:
		others=others+[imagelinks[zero]]
		zero=zero+1
print(colors.off+colors.bgwhite+colors.blue+" Success ! "+colors.off+colors.bold+colors.white+" Found "+colors.green+str(len(jpg))+colors.white+" jpgs and "+colors.green+str(len(png))+colors.white+" pngs "+ " As well as "+colors.green+str(len(others))+colors.white+" other formats")
print(" \n \n")
fore=input(" For Downloading Jpg input "+ colors.green+"j \n"+colors.white+ " for png input "+ colors.green+"p \n"+colors.white+" for other formats input "+colors.green+"o \n"+colors.white+" and for all image input "+colors.green+"a   "+colors.white)
print("\n\n")
try:
	if fore=="j":
		print(" Preparing to download jpg's ...")
	elif fore=="p":
		print(" Preparing to download png's ...")
	elif fore=="a":
		print(" Preparing to download all ...")
	elif fore=="o":
		print(" Preparing to download other formats ...")
	else:
		print(" Choose p , j , o or a")
except:
	print(" Choose p , j or a ")
	exit()
#works remains
print(colors.green+"***************************************")
print(colors.white+" You can download all of a format together \n Describe a range i.e. 5-10 of 40 \n or and random number of images")
wish=input(" Type "+colors.green+ "a"+ colors.white+" for all ,"+colors.green +"c "+colors.white+ "for range ,"+colors.green+ "r "+colors.white+"for random")
if wish=="a":
	if fore=="j":
		print(" Downloading "+str(len(jpg))+" Jpg's")
		zero=0
		while zero<len(jpg):
			dlink="wget "+jpg[zero]
			os.system(dlink)
			zero=zero+1
	elif fore=="p":
		print(" Downloading "+str(len(png))+" Png's")
		zero=0
		while zero<len(png):
			dlink="wget "+png[zero]
			os.system(dlink)
			zero=zero+1
	elif fore=="o":
		print(" Downloading "+str(len(others))+" others")
		zero=0
		while zero<len(others):
			dlink="wget "+others[zero]
			os.system(dlink)
			zero=zero+1
	elif fore=="a":
		print(" Downloading "+str(len(imagelinks))+" images")
		k=jpg+png+others
		zero=0
		while zero<len(k):
			dlink="wget "+k[zero]
			os.system(dlink)
			zero=zero+1
elif wish=="c":
	print(" Downloading in range ...")
	a=int(input(" lower range : "))
	b=int(input(" higher range : "))
	if fore=="j":
		print(" Downloading "+str(a)+" to "+str(b)+str(len(jpg))+" Jpg's")
		try:
			while a<=b:
				dlink="wget "+jpg[a]
				os.system(dlink)
				a=a+1
		except:
			print(" Error Occured . Must be wrong statement")
	elif fore=="p":
		print(" Downloading "+str(a)+" to "+str(b)+str(len(png))+" Png's")
		try:
			while a<=b:
				dlink="wget "+png[a]
				os.system(dlink)
				a=a+1
		except:
			print(" Error Occured . Must be wrong statement")
	elif fore=="o":
		print(" Downloading "+str(a)+" to "+str(b)+str(len(others))+" others")
		try:
			while a<=b:
				dlink="wget "+others[a]
				os.system(dlink)
				a=a+1
		except:
			print(" Error Occured . Must be wrong statement")
	elif fore=="a":
		print(" Downloading "+str(a)+" to "+str(b)+str(len(imagelinks))+" images")
		k=jpg+png+others
		try:
			while a<=b:
				dlink="wget "+k[a]
				os.system(dlink)
				a=a+1
		except:
			print(" Error Occured . Must be wrong statement")
elif wish=="r":
	print(" Downloading in Random ...")
	if fore=="j":
		num1=random.randint(0,(len(jpg)-1))
		num2=random.randint(0,(len(jpg)-1))
		if num1<num2:
			print(" Downloading image in range "+num1+"-"+num2)
			while num1<=num2:
				dlink="wget "+jpg[num1]
				os.system(dlink)
				num1=num1+1
		else:
			print(" Downloading image in range "+str(num2)+"-"+str(num1))
			while num2<=num1:
				dlink="wget "+jpg[num2]
				os.system(dlink)
				num2=num2+1
	elif fore=="p":
		num1=random.randint(0,(len(png)-1))
		num2=random.randint(0,(len(png)-1))
		if num1<num2:
			print(" Downloading image in range "+str(num1)+"-"+str(num2))
			while num1<=num2:
				dlink="wget "+png[num1]
				os.system(dlink)
				num1=num1+1
		else:
			print(" Downloading image in range "+str(num2)+"-"+str(num1))
			while num2<=num1:
				dlink="wget "+png[num2]
				os.system(dlink)
				num2=num2+1
	elif fore=="a":
		k=jpg+png+others
		num1=random.randint(0,(len(k)-1))
		num2=random.randint(0,(len(k)-1))
		if num1<num2:
			print(" Downloading image in range "+str(num1)+"-"+str(num2))
			while num1<=num2:
				dlink="wget "+k[num1]
				os.system(dlink)
				num1=num1+1
		else:
			print(" Downloading image in range "+str(num2)+"-"+str(num1))
			while num2<=num1:
				dlink="wget "+k[num2]
				os.system(dlink)
				num2=num2+1
	elif fore=="o":
		print(" Preparing to download other formats ...")
	else:
		print(" Choose p , j , o or a")
	


