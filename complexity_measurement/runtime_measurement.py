import math
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('calc.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class TimeoutError(Exception):
    pass


class runtime_calculation:
    def __init__(self, fun, x=[i for i in range(1, 100)]):
        self.fun = fun
        self.y = []
        self.x = x

    def measure_one_call(self, n):
        start_time = time.time()
        self.f(n)
        return time.time() - start_time

    def measure_reliance(self, max_time=30, log_info = 10):
        time_sum = 0
        for i in range(len(self.x)):
            self.y.append(self.measure_one_call(self.x[i]))
            time_sum += self.y[i]
            if i % log_info == 0:
                logger.info("%d measurements made in %f " % (log_info, sum(self.y[i - log_info:i])))

            if time_sum >= max_time:
                logger.error("Computations overdue time limitation, last n is %d ", self.x[i])
                raise TimeoutError("Computations overdue time limitation")
        return self.x, self.y
