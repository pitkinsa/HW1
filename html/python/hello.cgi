#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import os
import time

def getSortedEnvVars():
	list = os.environ.keys()
	list.sort()
	return list

def printGreeting():
	print ("Content-Type: text/html;charset-utf-8")
	print ("")
	print ("<h1>Hello World from Python @ {}</h1>".format())

def main():
	cgitb.enable()
	
	print("")
	print("<table>")
	for param in getSortedEnvVars():
		print "<tr><td><b>%s</b></td> <td>%s</td></tr>\n" % (param, os.environ[param])
	print("</table>")

if __name__ == "__main__":
	main()