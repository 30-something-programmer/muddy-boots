#!/usr/bin/python 
from threading import Thread
from modules.config import config
import sys
from modules.runtime import running
from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
	"""
		Handles exit requests to ensure clean exit
	"""
	print('SIGINT or CTRL-C detected. Exiting gracefully')
	exit(0)

# Begin the app
if __name__ == '__main__': 
	
	running_apps = []
	try:
		# Start the websocket server in a seperate thread
		if config["website"]["enable"]:
			name = "Muddy Boots Website"
			running_apps.append((name, config["website"]))
			from modules.website import website_server
			Thread(
				name = name, 
				target = website_server, 
				daemon = True
			).start()

		# Start the website in a seperate thread
		if config["websocket"]["enable"]:
			name = "Muddy Boots Websocket"
			running_apps.append((name, config["websocket"]))
			from modules.websocket import websocket_server
			Thread(
				name = name, 
				target = websocket_server, 
				daemon = True
			).start()

	except SystemExit:
		raise
	
	except Exception as e:
		print(f"exception -- {e}")
		sys.exit(1)

	
	# Tell Python to run the handler() function when SIGINT is recieved
	signal(SIGINT, handler)

	print('Running the following apps:')
	for app in running_apps:
		print(f"  - {app[0]}:{app[1]}")
	print('Press CTRL-C to exit.')

	while running:
        # Do nothing and hog CPU forever until SIGINT received.
		pass