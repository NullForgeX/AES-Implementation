import unittest

from aes.core import encrypt_block, decrypt_block


class TestCore(unittest.TestCase):
    def test_encrypt_then_decrypt(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")

        ciphertext = encrypt_block(plaintext, key)
        recovered = decrypt_block(ciphertext, key)

        self.assertEqual(recovered, plaintext)

    def test_invalid_plaintext_length(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        with self.assertRaises(ValueError):
            encrypt_block(b"short", key)

    def test_invalid_key_length(self):
        plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")
        with self.assertRaises(ValueError):
            encrypt_block(plaintext, b"short")

    def test_invalid_ciphertext_length(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        with self.assertRaises(ValueError):
            decrypt_block(b"short", key)

    def test_invalid_key_length_for_decryption(self):
        ciphertext = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")
        with self.assertRaises(ValueError):
            decrypt_block(ciphertext, b"short")


if __name__ == "__main__":
    unittest.main()
