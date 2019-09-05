def convert(conversions, start, end):
    """
    Given a conversion structure, perform a constant-time conversion
    """
    try:
        start_root, start_rate = conversions[start]
        end_root, end_rate = conversions[end]
    except KeyError as e:
        print('Encountered KeyError: {}'.format(e))
        return None

    if start_root != end_root:
        return None

    return end_rate / start_rate