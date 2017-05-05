import math
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('calc.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class UnsuportedError(Exception):
    pass


class complexity_solver(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def linear(self, x):
        return x

    def square(self, x):
        return x * x

    def n_logn(self, x):
        return x * math.log(x)

    def aprox_quality(self, x, y, fun):
        return abs(np.polyfit([fun(i) for i in x], y, 1)[1])

    def bestMatch(self, x, y):
        dev_lin = self.aprox_quality(x, y, self.linear)
        dev_log = self.aprox_quality(x, y, self.n_logn)
        dev_cub = self.aprox_quality(x, y, self.square)

        if dev_lin < dev_log and dev_lin < dev_cub:
            logger.info("Detected: Linear Complexity")
            print("Linear Complexity")
            return self.linear

        if dev_log < dev_cub and dev_log < dev_lin:
            logger.info("Detected: N*LOG(N) Complexity")
            print("N*LOG(N) Complexity")
            return self.n_logn

        logger.info("Detected: N*N Complexity")
        print("N*N Complexity")
        return self.square

    def print_fun(self, f):
        if f == self.square:
            return "N^2"
        elif f == self.n_logn:
            return "N*LOG(N)"
        elif f == self.linear:
            return "N"
        logger.error("Print function cannot support this function")
        raise UnsuportedError("Argument is not supported")

    def time_aprox(self, x, y, f):
        z = np.polyfit([f(a) for a in x], y, 1)
        print("T = %+.2f * (%s) %+.2f " % (z[0], self.print_fun(f), z[1]))

    def complx_aprox(self, x, y, f):
        z = np.polyfit([f(a) for a in x], y, 1)
        rootStr = ("(T %+.2f)/(%.2f)" % (z[1], z[0]))

        if f == self.linear:
            print("N = " + rootStr)
            return
        elif f == self.square:
            print("N = sqrt(" + rootStr + ")")
            return

        raise UnsuportedError("Unknown inverse function")

    def compute_res(self):
        logger.info("Calculate complexity")
        fun = self.bestMatch(self.x, self.y)
        logger.info("Present time function")
        self.time_aprox(self.x, self.y, fun)
        try:
            self.complx_aprox(self.x, self.y, fun)
            logger.info("Present complexity function")
        except UnsuportedError:
            logger.warning("Cant calculate complexity, unknown inverse function")
            print("Cannot present complexity function due to complicated inverse function")

