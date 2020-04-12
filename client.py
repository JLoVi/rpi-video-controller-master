#! /usr/bin/env python3

import socket
import json
import sys

print sys.argv
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '172.168.0.3'
PORT = 5000
x = None
if len(sys.argv) > 1:
	message = sys.argv[1]
	s.connect((HOST, PORT))
	
	if message == 'START_PLAYLIST':
		print('starting playlist')
		x = {
			"ids": ["1","2","3"],
			"message": message
		}
	elif message == 'START_STREAM':
		x = {
			"id" : "1",
			"message": message
		}
	elif message == 'STOP_PLAYLIST':
		print('stopping playlist')
		x = {
			"message": message
		}
	elif message == 'STOP_STREAM':
		print('stopping stream')
		x = {
			"message": message
		}
	else:
		print('bad command')
		s.close()
	
	if x is not None:
		y = json.dumps(x)
		s.send(y)
		s.close();
