__author__ = 'mpetyx (Michael Petychakis)'
__version__ = "1.0.0"
__maintainer__ = "Michael Petychakis"
__email__ = "hello@apilama.com"
__status__ = "Production"


import grpc

# import the generated classes
import requests

# import the original calculator.py

class Client:

    def __init__(self, channel=None):

        pass


    def squareRoot(self, number):
        return requests.get('http://127.0.0.1:5000/int/'+str(number)).text

# import sys
# sys.path.append(".")
# import timer
#
#
# with timer.MyTimer():
#     print(Client().squareRoot(64))