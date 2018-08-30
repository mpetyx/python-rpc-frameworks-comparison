__author__ = 'mpetyx (Michael Petychakis)'
__version__ = "1.0.0"
__maintainer__ = "Michael Petychakis"
__email__ = "hello@apilama.com"
__status__ = "Production"

from client import Client

for number in range(1,100000):
    Client().squareRoot(number)