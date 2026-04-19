def hex_to_bytes(hex_string):
    hex_string = hex_string.strip().replace(" ", "")
    return bytes.fromhex(hex_string)


def bytes_to_hex(data):
    return data.hex()


def bytes_to_state(block):
    if len(block) != 16:
        raise ValueError("AES block must be exactly 16 bytes")

    state = [[0] * 4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        state[row][col] = block[i]
    return state


def state_to_bytes(state):
    output = bytearray(16)
    for col in range(4):
        for row in range(4):
            output[col * 4 + row] = state[row][col]
    return bytes(output)


def xor_words(a, b):
    return [x ^ y for x, y in zip(a, b)]