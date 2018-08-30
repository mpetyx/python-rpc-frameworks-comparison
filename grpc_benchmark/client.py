__author__ = 'mpetyx (Michael Petychakis)'
__version__ = "1.0.0"
__maintainer__ = "Michael Petychakis"
__email__ = "hello@apilama.com"
__status__ = "Production"


import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

class Client:

    def __init__(self, channel=None):

        if not channel:
            # open a gRPC channel
            channel = grpc.insecure_channel('localhost:50051')
        else:
            channel = grpc.insecure_channel(channel)

        # create a stub (client)
        self.stub = calculator_pb2_grpc.CalculatorStub(channel)

    def squareRoot(self, number):
        # create a valid request message
        number = calculator_pb2.Number(value=number)

        # make the call
        response = self.stub.SquareRoot(number)

        # et voilà
        # print(response.value)

        return response.value

