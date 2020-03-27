# -*- coding: utf-8 -*-
#Version: 1.0.0
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

import os
import sys
import urllib, re






enlaces = (['http://example1.com','http://example2.com']) #Modify with your list of domains.

for enlace in enlaces:

	
	scan = enlace
	os.system("@echo off")
	os.system("curl -L -m 10 %s > tmp.html" %scan)
	code = "tmp.html"
	lines = urllib.urlopen(code).read()

	enlas = re.findall('http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', lines)
	f=open("logs.txt","a")
	f.write("Domain: "+scan+ "\nEnlaces:\n"+str(enlas)+"\nDetected keywords: ")
	f.close()
	
	words = (['keyword','keyword2']) #Modify with your list of keywords
	print("Domain: "+enlace)
	print("Detected keywords:")

	for busqueda in words:
		
		search = lines.find(busqueda) 
		if search != -1:
			print(busqueda)
			f=open("logs.txt","a")
			f.write(busqueda+",")
			f.close()


	print("Links: ")
	print(enlas)
  	f=open("logs.txt","a")
	f.write("\n")
	f.close()

    
				
		


