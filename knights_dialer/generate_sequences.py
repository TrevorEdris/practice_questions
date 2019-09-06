from neighbors import neighbors


NUM_HOPS = 10


def yeild_sequences(starting_position, num_hops, sequence=None):
    if sequence is None:
        sequence = [starting_position]

    print('start: {}\tsequence: {}\tnum_hops: {}'.format(starting_position, sequence, num_hops))

    if num_hops == 0:
        yield sequence
        return

    for neighbor in neighbors(starting_position):
        print('Found neighbor {}'.format(neighbor))
        yield yeild_sequences(
            neighbor, num_hops - 1, sequence + [neighbor]
        )


def count_sequences(starting_position, num_hops):
    num_sequences = 0
    for _ in yeild_sequences(starting_position, num_hops):
        num_sequences += 1
    return num_sequences


if __name__ == '__main__':
    for i in range(0, 10):
        print('============[ {} - NUM_HOPS: {} ]============'.format(i, NUM_HOPS))
        num = count_sequences(i, NUM_HOPS)
        print('num_sequences: {}\n'.format(num))
