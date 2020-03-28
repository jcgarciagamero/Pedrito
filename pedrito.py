# -*- coding: utf-8 -*-
#Version: 1.0.1
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

import os
import sys
import urllib.request, urllib.parse, urllib.error, re

print('  ____   U _____ u____    ____                 _____   U  ___ u ')
print('U|  _"\ u\| ___"|/  _"\\U |  _"\ u     ___     |_ " _|   \/"_ \/ ')
print('\| |_) |/ |  _|"/| | | |\| |_) |/    |_"_|      | |     | | | | ')
print(' |  __/   | |___U| |_| |\|  _ <       | |      /| |\.-,_| |_| | ')
print(' |_|      |_____||____/ u|_| \_\    U/| |\\u   u |_|U \_)-\___/  ')
print(' ||>>_    <<   >> |||_   //   \\_.-,_|___|_,-._// \\_     \\    ')
print('(__)__)  (__) (__|__)_) (__)  (__)\_)-' '-(_/(__) (__)   (__)   ')




enlaces = (['http://example1.com','http://example2.com']) #Modify with your list of domains.

for enlace in enlaces:

	var = 0
	scan = enlace
	os.system("curl -L -m 10 %s > tmp.txt" %scan)
	
	f = open ('tmp.txt','r',encoding='utf-8')
	lines = f.read()
	f.close()

	
	
	words = (['keyword','keyword2']) #Modify with your list of keywords
	print(("Domain: "+enlace))
	print("Detected keywords:")

	for busqueda in words:
		
		search = lines.find(busqueda) 
		if search != -1:
			print(busqueda)
			if var != 1:
				enlas = re.findall('http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', lines)
				f=open("logs.txt","a")
				f.write("Domain: "+scan+ "\nEnlaces:\n"+str(enlas)+"\nDetected keywords: \n")
				f.close()
				f=open("logs.txt","a")
				f.write(busqueda+",")
				f.close()
				print("Links: ")
				print(enlas)
				f=open("logs.txt","a")
				f.write("\n")
				f.close()

				var = 1
			else:
				f=open("logs.txt","a")
				f.write(busqueda+",")
				f.close()
				f=open("logs.txt","a")
				f.write("\n")
				f.close()
		
