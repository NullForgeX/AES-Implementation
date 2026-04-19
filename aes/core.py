from .key_schedule import expand_key
from .operations import (
    add_round_key,
    sub_bytes,
    inv_sub_bytes,
    shift_rows,
    inv_shift_rows,
    mix_columns,
    inv_mix_columns,
)
from .utils import bytes_to_state, state_to_bytes


def encrypt_block(plaintext, key):
    if len(plaintext) != 16:
        raise ValueError("Plaintext block must be exactly 16 bytes")
    if len(key) != 16:
        raise ValueError("AES-128 key must be exactly 16 bytes")

    state = bytes_to_state(plaintext)
    round_keys = expand_key(key)

    add_round_key(state, round_keys[0])

    for round_num in range(1, 10):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, round_keys[round_num])

    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, round_keys[10])

    return state_to_bytes(state)


def decrypt_block(ciphertext, key):
    if len(ciphertext) != 16:
        raise ValueError("Ciphertext block must be exactly 16 bytes")
    if len(key) != 16:
        raise ValueError("AES-128 key must be exactly 16 bytes")

    state = bytes_to_state(ciphertext)
    round_keys = expand_key(key)

    add_round_key(state, round_keys[10])

    for round_num in range(9, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, round_keys[round_num])
        inv_mix_columns(state)

    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, round_keys[0])

    return state_to_bytes(state)