from neighbors import neighbors, NEIGHBORS_MATRIX


function_calls = {
    'count_sequence_calls': 0,
    'count_with_cache_calls': 0,
    'count_with_dp_calls': 0,
    'count_with_matrix_calls': 0,
}


def count_sequences(start, num_hops):
    global function_calls
    function_calls['count_sequence_calls'] += 1
    if num_hops == 0:
        return 1

    num_sequences = 0
    for position in neighbors(start):
        num_sequences += count_sequences(position, num_hops - 1)
    return num_sequences


def count_with_cache(start, num_hops):
    cache = {}

    def helper(position, num_hops):
        global function_calls
        function_calls['count_with_cache_calls'] += 1
        if (position, num_hops) in cache:
            return cache[ (position, num_hops) ]

        if num_hops == 0:
            return 1

        num_sequences = 0
        for neighbor in neighbors(position):
            num_sequences += helper(neighbor, num_hops - 1)
        cache[ (position, num_hops) ] = num_sequences
        return num_sequences

    return helper(start, num_hops)


def count_with_dp(start, num_hops):
    global function_calls
    prior_case = [1] * 10
    current_case = [0] * 10
    current_num_hops = 1

    while current_num_hops <= num_hops:
        function_calls['count_with_dp_calls'] += 1
        current_case = [0] * 10
        current_num_hops += 1

        for position in range(10):
            for neighbor in neighbors(position):
                current_case[position] += prior_case[neighbor]
        prior_case = current_case

    return current_case[start]


def matrix_multiply(A, B):
    A_rows, A_cols = len(A), len(A[0])
    B_rows, B_cols = len(B), len(B[0])
    result = list(map(lambda i: [0] * B_cols, range(A_rows)))

    for row in range(A_rows):
        for col in range(B_cols):
            for i in range(B_rows):
                result[row][col] += A[row][i] * B[i][col]

    return result


# NOTE: This function produces a different result than the other 3 functions
def count_with_matrix(start, num_hops):
    global function_calls
    # Start off with a 10x10 identity matrix
    accum = [[1 if i == j else 0 for i in range(10)] for j in range(10)]
    power_of_2 = None

    # bin(num_hops) starts with "0b", slice it off with [2:]
    for bit_num, bit in enumerate(reversed(bin(num_hops)[2:])):
        function_calls['count_with_matrix_calls'] += 1
        if bit_num == 0:
            import copy
            power_of_2 = copy.deepcopy(NEIGHBORS_MATRIX)
        else:
            power_of_2 = matrix_multiply(power_of_2, power_of_2)

        if bit == '1':
            accum = matrix_multiply(accum, power_of_2)

    return matrix_multiply(accum, [[1]]*10)[start][0]

