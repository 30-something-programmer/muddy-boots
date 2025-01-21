from modules.api import api_server
from modules.runtime import running

if __name__ == '__main__': 
    api_server()

    print('Press CTRL-C to exit.')

    while running:
        # Do nothing and hog CPU forever until SIGINT received.
        pass