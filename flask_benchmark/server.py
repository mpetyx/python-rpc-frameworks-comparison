__author__ = 'mpetyx (Michael Petychakis)'
__version__ = "1.0.0"
__maintainer__ = "Michael Petychakis"
__email__ = "hello@apilama.com"
__status__ = "Production"


# import the original calculator.py
import sys
sys.path.append(".")
import calculator

from flask import Flask
app = Flask(__name__)

@app.route("/int/<int:number>")
def squareRoot(number):
    return str(calculator.square_root(number))