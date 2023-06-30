import unittest
from src.Huffman_coding import HuffmanCoding

class HuffmanCodingTestCase(unittest.TestCase):
    def test_encode(self):
        huffman = HuffmanCoding()

        # Caso de prueba 1
        text1 = "mi pasion es programar"
        expected_encoded_text1 = "110111100111111100000111000101000110101000011111110100111001011001101100101"
        huffman.build_tree(text1)
        encoded_text1 = huffman.encode(text1)
        self.assertEqual(encoded_text1, expected_encoded_text1)


if __name__ == "__main__":
    unittest.main()
