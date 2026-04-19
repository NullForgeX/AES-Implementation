from .operations import S_BOX
from .utils import xor_words

RCON = [
    0x00,
    0x01, 0x02, 0x04, 0x08, 0x10,
    0x20, 0x40, 0x80, 0x1B, 0x36
]


def rot_word(word):
    return word[1:] + word[:1]


def sub_word(word):
    return [S_BOX[b] for b in word]


def expand_key(key_bytes):
    if len(key_bytes) != 16:
        raise ValueError("AES-128 key must be exactly 16 bytes")

    words = []
    for i in range(4):
        words.append([
            key_bytes[4 * i],
            key_bytes[4 * i + 1],
            key_bytes[4 * i + 2],
            key_bytes[4 * i + 3],
        ])

    for i in range(4, 44):
        temp = words[i - 1][:]

        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[i // 4]

        words.append(xor_words(words[i - 4], temp))

    round_keys = []
    for round_index in range(11):
        round_words = words[round_index * 4:(round_index + 1) * 4]
        round_keys.append(round_words)

    return round_keys