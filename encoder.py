def encode(n, bit_length=None):
    binary_str = bin(n)[2:]
    binary_list = [bool(int(bit)) for bit in binary_str]

    if bit_length is not None:
        current_bit_length = len(binary_list)
        if bit_length > current_bit_length:
            binary_list = [False] * (bit_length - current_bit_length) + binary_list

    return binary_list
