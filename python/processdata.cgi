#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb, cgi

def main():
	cgitb.enable()
	print ("Content-Type: text/html;charset-utf-8")
	print ("")
	form = cgi.FieldStorage()
	try:
		username = validateString(form.getvalue('username'))
		password = validateString(form.getvalue('password'))
		magicnum1 = validateInt(form.getvalue('magicnum'))
	except ValueError:
		print("<p>There was an error with your input</p>")
	else:
		s = "<h1>Hello {} with a password of {}</h1></br>".format(username,password)
		s = s * magicnum1
		print(s)

def validateString(string):
	return str(string)
def validateInt(string):
	return int(string)
if __name__ == "__main__":
	main()