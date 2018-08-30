__author__ = 'mpetyx (Michael Petychakis)'
__version__ = "1.0.0"
__maintainer__ = "Michael Petychakis"
__email__ = "hello@apilama.com"
__status__ = "Production"

from client import Client

import sys
sys.path.append(".")
import timer

number_of_clients = 1000
with timer.MyTimer(): #context={"framework":"flask","clients":number_of_clients}):
    for number in range(1,number_of_clients):
        Client().squareRoot(number)