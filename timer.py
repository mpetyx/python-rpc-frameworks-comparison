__author__ = 'mpetyx (Michael Petychakis)'
__version__ = "1.0.0"
__maintainer__ = "Michael Petychakis"
__email__ = "hello@apilama.com"
__status__ = "Production"

import time
from pprint import pprint
from datetime import datetime

class MyTimer():
    """
    This is a custom object for benchmarking python code
    """
    def __init__(self, context=None):
        self.start = time.time()
        if context is None:
            context = {}
        self.context = context

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = end - self.start
        msg = 'The function took {time} seconds to complete'
        print(msg.format(time=runtime))

        pprint(
            {
                ** {
                    "timerun": runtime,
                },
                "datetime":str(datetime.now()),
                ** self.context
            }
        )
        # TODO save the object in redis