import sys

from aes.core import encrypt_block, decrypt_block
from aes.utils import hex_to_bytes, bytes_to_hex


def print_usage():
    print("Usage:")
    print("  python main.py encrypt <plaintext_hex> <key_hex>")
    print("  python main.py decrypt <ciphertext_hex> <key_hex>")


def main():
    if len(sys.argv) != 4:
        print_usage()
        return

    mode = sys.argv[1].lower()
    data_hex = sys.argv[2]
    key_hex = sys.argv[3]

    try:
        data = hex_to_bytes(data_hex)
        key = hex_to_bytes(key_hex)

        if len(data) != 16:
            raise ValueError("Input must be exactly 16 bytes (32 hex characters)")
        if len(key) != 16:
            raise ValueError("Key must be exactly 16 bytes (32 hex characters)")

        if mode == "encrypt":
            result = encrypt_block(data, key)
            print("Ciphertext:", bytes_to_hex(result))
        elif mode == "decrypt":
            result = decrypt_block(data, key)
            print("Plaintext:", bytes_to_hex(result))
        else:
            print("Mode must be 'encrypt' or 'decrypt'")
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()