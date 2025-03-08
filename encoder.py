def binary_encode(n, bit_length=None):
    binary_str = bin(n)[2:]
    binary_list = [bool(int(bit)) for bit in binary_str]

    if bit_length is not None:
        current_bit_length = len(binary_list)
        if bit_length > current_bit_length:
            binary_list = [False] * (bit_length - current_bit_length) + binary_list

    return binary_list


def shape_movement_dir(tuple, b):
    coord_1 = tuple[0]
    coord_2 = tuple[1]
    return_values = {
        0: (coord_1 + 1, coord_2),
        1: (coord_1 - 1, coord_2),
        2: (coord_1, coord_2 + 1),
        3: (coord_1, coord_2 - 1),
    }
    return return_values[b]


def sim_setup():
    return True
