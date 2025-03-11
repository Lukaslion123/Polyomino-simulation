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

    return tuple(binary_list)


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


def shape_overallcoords(shape):
    """rewrites the coordinates of a shape to start in the top left corner"""
    list_x = []
    list_y = []
    for coord in shape:
        list_x.append(coord[0])
        list_y.append(coord[1])
    min_x = min(list_x)
    min_xc = min_x
    max_x = max(list_x)
    min_y = min(list_y)
    min_yc = min_y
    max_y = max(list_y)
    dict_x = {}
    for d in range(max_x - min_x + 1):
        dict_x[min_xc] = d
        min_xc += 1
    dict_y = {}
    for d in range(max_y - min_y + 1):
        dict_y[min_yc] = d
        min_yc += 1
    unordered = []
    for coord in shape:
        unordered.append((dict_x[coord[0]], dict_y[coord[1]]))
        new_shape = sorted(unordered, key=lambda x: (x[0], x[1]))
    return new_shape


def shape_rotate(shape):
    """rotates a shape 90 degrees clockwise"""
    new_shape = []
    for coord in shape:
        new_coord = (coord[1], -coord[0])
        new_shape.append(new_coord)
    return shape_overallcoords(new_shape)


def shape_mirror(shape):
    """mirrors a shape along the x-axis"""
    new_shape = []
    for coord in shape:
        new_coord = (-coord[0], coord[1])
        new_shape.append(new_coord)
    return shape_overallcoords(new_shape)


def shape_check_directions(overlay_shape, coord, reverse=False):
    """checks for which squares are free around the current base
    shape of n-1 and returns them for further use"""
    squares = []
    for b in range(4):
        coords = shape_movement_dir(coord, b)
        if not reverse:
            if not coords in overlay_shape:
                squares.append(coords)
        else:
            if coords in overlay_shape:
                squares.append(coords)
    return squares
