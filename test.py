import math


class test(object):
    def __init__(self, args):
        if (len(args) > 0):
            self.x = args[0]
        if (len(args) > 1):
            self.y = args[1]
        if (len(args) > 2):
            self.str = args[2]

    def linear(self, x):
        for _ in range(0, x):
            1 + 1

    def square(self, x):
        for _ in range(0, x * x):
            1 + 1

    def nLogN(self, x):
        for _ in range(0, int(x * math.log(x))+1):
            1 + 1


