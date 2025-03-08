def binary_encode(n, bit_length=None):
    binary_str = bin(n)[2:]
    binary_list = [bool(int(bit)) for bit in binary_str]

    if bit_length is not None:
        current_bit_length = len(binary_list)
        if bit_length > current_bit_length:
            binary_list = [False] * (bit_length - current_bit_length) + binary_list

    return binary_list


def shape_movement_dir(b):
    if b == 0:
        return [1, 0]
    elif b == 1:
        return [0, 1]
    elif b == 2:
        return [-1, 0]
    elif b == 3:
        return [0, -1]


def sim_setup():
    return True
