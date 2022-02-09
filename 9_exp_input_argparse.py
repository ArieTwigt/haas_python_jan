from our_functions.calculation_functions import calc_circle
import argparse

# initiate an arg parser
parser = argparse.ArgumentParser()

# add arguments to the arg parser
parser.add_argument('--diameter', type=int, required=True)
parser.add_argument('--multiplier', type=float, required=False, default=1)

# create the arg parser
args = parser.parse_args()

if __name__ == '__main__':
    diameter   = args.diameter
    multiplier = args.multiplier
    result = calc_circle(diameter=diameter, multiplier=multiplier)
    print(result)