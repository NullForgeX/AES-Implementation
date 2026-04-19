import unittest

from aes.core import encrypt_block, decrypt_block


class TestVectors(unittest.TestCase):
    def test_known_aes_128_vector(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")
        expected_ciphertext = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")

        ciphertext = encrypt_block(plaintext, key)

        self.assertEqual(ciphertext, expected_ciphertext)

    def test_known_aes_128_vector_decryption(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        ciphertext = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")
        expected_plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")

        plaintext = decrypt_block(ciphertext, key)

        self.assertEqual(plaintext, expected_plaintext)


if __name__ == "__main__":
    unittest.main()