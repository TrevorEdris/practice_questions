import argparse
import json

from bfs import make_conversions
from converter import convert
from rate_graph import RateGraph



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('origin_value', type=float, help='The value to convert')
    parser.add_argument('origin_unit', type=str, help='The starting unit')
    parser.add_argument('dest_unit', type=str, help='The unit to convert to')
    parser.add_argument('-i', '--input', type=str, default='conversion_rates.txt', help='Full filepath to the input file')
    args = parser.parse_args()

    # Step 0: Read the input file
    with open(args.input) as f:
        raw_data = f.readlines()

    # Step 1: Process the raw data into a usable format
    multiplier_data = []
    for line in raw_data:
        line = line.strip('\n')
        if not line or line.startswith('#'):
            continue
        line_data = line.split(' ')
        if len(line_data) != 3:
            continue
        start, end, rate = line_data
        rate = float(rate)
        multiplier_data.append((start, end, rate))

    # Step 2: Build the Rate graph
    rate_graph = RateGraph(multiplier_data)

    # Step 3: Build the constant-time conversion graph
    conversions = make_conversions(rate_graph)

    # Sttep 4: Find the appropriate multiplier
    multiplier = convert(conversions, args.origin_unit, args.dest_unit)

    # Step 5: Perform the conversion
    if multiplier is not None:
        conversion_result = multiplier * args.origin_value
        print('{} {} converted to {} = {}'.format(args.origin_value, args.origin_unit, args.dest_unit, conversion_result))
    else:
        print('No conversion found')
