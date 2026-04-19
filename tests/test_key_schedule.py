import unittest

from aes.key_schedule import rot_word, sub_word, expand_key


class TestKeySchedule(unittest.TestCase):
    def test_rot_word(self):
        self.assertEqual(rot_word([0x09, 0xCF, 0x4F, 0x3C]), [0xCF, 0x4F, 0x3C, 0x09])

    def test_sub_word(self):
        self.assertEqual(sub_word([0xCF, 0x4F, 0x3C, 0x09]), [0x8A, 0x84, 0xEB, 0x01])

    def test_expand_key_round_count(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        round_keys = expand_key(key)
        self.assertEqual(len(round_keys), 11)

    def test_first_round_key_is_original_key(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        round_keys = expand_key(key)

        expected = [
            [0x00, 0x01, 0x02, 0x03],
            [0x04, 0x05, 0x06, 0x07],
            [0x08, 0x09, 0x0A, 0x0B],
            [0x0C, 0x0D, 0x0E, 0x0F],
        ]
        self.assertEqual(round_keys[0], expected)


if __name__ == "__main__":
    unittest.main()