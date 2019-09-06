import argparse
from count import (
    count_sequences,
    count_with_cache,
    count_with_dp,
    count_with_matrix,
    function_calls
)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('hops', type=int, help='Number of hops to make (0-15)')
    args = parser.parse_args()

    if args.hops > 15:
        print('Hops should be less than 15 due to the recursive limitations')
        exit(1)
    elif args.hops < 0:
        print('Hops should be a value between 0 and 15')
        exit(1)

    for i in range(10):
        count_sequence_calls = 0
        count_with_cache_calls = 0
        count_with_dp_calls = 0
        print('=======================[ {} ]==================================='.format(i))

        print('  count_sequences({}, {}) = {:4d} ({:3d} function calls)'.format(
            i, args.hops, count_sequences(i, args.hops), function_calls['count_sequence_calls']))

        print(' count_with_cache({}, {}) = {:4d} ({:3d} function calls)'.format(
            i, args.hops, count_with_cache(i, args.hops), function_calls['count_with_cache_calls']))

        print('    count_with_dp({}, {}) = {:4d} ({:3d} iterations)'.format(
            i, args.hops, count_with_dp(i, args.hops), function_calls['count_with_dp_calls']))

        print('count_with_matrix({}, {}) = {:4d} ({:3d} iterations)'.format(
            i, args.hops, count_with_matrix(i, args.hops), function_calls['count_with_matrix_calls']))
