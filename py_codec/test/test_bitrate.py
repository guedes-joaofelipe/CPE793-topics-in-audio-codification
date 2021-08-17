import unittest
from lib.bitrate import compute_bitrate


class TestBitrate(unittest.TestCase):
    def test_simple_values(self):
        self.assertEqual(compute_bitrate(1, 1, 1), 1)
        self.assertEqual(compute_bitrate(1, 2, 3), 6)
        self.assertRaises(AssertionError, compute_bitrate, 0, 0, 0)
        self.assertRaises(AssertionError, compute_bitrate, -1, -1, -1)

    def test_common_values(self):
        self.assertEqual(compute_bitrate(1, 8000, 8) / 1000, 64)
        self.assertEqual(compute_bitrate(2, 44100, 16) / 1000, 1411.2)
        self.assertEqual(compute_bitrate(5, 44100, 16) / 1000, 3528)
        self.assertEqual(compute_bitrate(5, 96000, 24) / 1000, 11520)


if __name__ == '__main__':
    unittest.main()
