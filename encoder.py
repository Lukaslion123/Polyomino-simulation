"""does behind the scenes calculations for preparing
between diffrent scripts, handles hardcode requests and encodes binary"""


def binary_encode(n, bit_length=None):
    """Converts an integer to a binary list of booleans"""
    binary_str = bin(n)[2:]
    binary_list = [bool(int(bit)) for bit in binary_str]

    if bit_length is not None:
        current_bit_length = len(binary_list)
        if bit_length > current_bit_length:
            binary_list = [False] * (bit_length - current_bit_length) + binary_list

    return binary_list


def shape_movement_dir(val, b):
    """returns a tuple representing a coordinate
    of a space in a set direction from a given coordinate"""
    coord_1 = val[0]
    coord_2 = val[1]
    return_values = {
        0: (coord_1 + 1, coord_2),
        1: (coord_1 - 1, coord_2),
        2: (coord_1, coord_2 + 1),
        3: (coord_1, coord_2 - 1),
    }
    return return_values[b]


def sim_setup():
    """fill a give shape with the binary values to be used in the simulation"""
    return True
