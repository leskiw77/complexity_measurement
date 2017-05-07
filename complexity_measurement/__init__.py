import argparse

# import matplotimpolib.pyplot as plt

from complexity_measurement.complexity_indicator import complexity_solver
from complexity_measurement.runtime_measurement import runtime_calculation


def run(cls, init, run, dest="", dest_par=""):
    try:
        line = init.replace('[', '').replace(']', '').split(',')
        mod = __import__(cls)
        mod = getattr(mod, cls)
        cls = mod(line)
        fun = getattr(cls, run)
    except:
        print("Invalid input args")
        exit()

    rc = runtime_calculation(fun, range(1, 1000000, 10000))

    try:
        x, y = rc.measure_reliance()
    except:
        print("Execution last too long, only %d measurements acquired" % len(rc.y))
        if len(rc.y) < 5:
            print("Program must be terminate")
            exit()

        print("Program wont be terminated, but result might be incorrect")
        y = rc.y
        x = rc.x[:len(y)]

    cs = complexity_solver(x, y)
    cs.compute_res()

    # plt.plot(x, y, 'ro')
    # plt.show()

    if dest:
        try:
            line = []
            if dest_par is not None:
                line = dest_par.replace('[', '').replace(']', '').split(',')
            fun = getattr(cls, dest)
            fun(line)
        except:
            print("Error in destructor call")
    exit()


run('test', '', 'square')
