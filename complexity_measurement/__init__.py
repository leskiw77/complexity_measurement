import matplotlib.pyplot as plt

from complexity_measurement.complexity_indicator import complexity_solver
from complexity_measurement.runtime_measurement import runtime_calculation

def run():
    rc = runtime_calculation()

    try:
        x, y = rc.measure_reliance(10000, 10)
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

    plt.plot(x, y, 'ro')
    plt.show()
