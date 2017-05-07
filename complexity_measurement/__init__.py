import argparse

import matplotimpolib.pyplot as plt

from complexity_measurement.complexity_indicator import complexity_solver
from complexity_measurement.runtime_measurement import runtime_calculation


parser = argparse.ArgumentParser(prog="Big O notation", description='Estimate complexity of input program',
                                 epilog='Thanks for using program')

parser.add_argument("cls", help="class to run")
parser.add_argument("init", help="constructor argument without whitespaces e.g. [1,2,str], bracket might be omitted")
parser.add_argument("run", help="program to run")
parser.add_argument('-dest', help='cleaning function')
parser.add_argument('-dest_par', help='parameters of destructor')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

def run():
    rc = runtime_calculation()

    try:
        line = args.init.replace('[', '').replace(']', '').split(',')
        mod = __import__(args.cls)
        mod = getattr(mod, args.cls)
        cls = mod(line)
        fun = getattr(cls, args.run)
    except:
        print("Invalid input args")
        exit()

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


    if args.dest is not None:
        try:
            line = []
            if args.dest_par is not None:
                line = args.dest_par.replace('[', '').replace(']', '').split(',')
            fun = getattr(cls, args.dest)
            fun(line)
        except:
            print("Error in destructor call")