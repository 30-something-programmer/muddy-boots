# Main python script to run Muddy Boots.
# Will start the API and the GUI

#!/usr/bin/python 
from threading import Thread
from modules.mb_config import config
import sys
from modules.mb_runtime import running
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
	
	# Host a list of tuples with details of what apps are running
	running_apps = []
 
	try:
		
  		# Start the website in a seperate thread
		if config["website"]["enable"]:
			running_apps.append((config["website"]["name"], config["website"]))
			from modules.mb_website import website_server
			Thread(
				name = "Muddy Boots Website", 
				target = website_server, 
				daemon = True
			).start()

		# Start the api server in a seperate thread
		if config["api"]["enable"]:
			running_apps.append((config["website"]["name"], config["api"]))
			from modules.mb_api import api_server
			Thread(
				name = "Muddy Boots API", 
				target = api_server, 
				daemon = True
			).start()

		# Start the GUI in a seperate thread
		if config["gui"]["enable"]:
			print("we want a gui here. Ta")
			
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