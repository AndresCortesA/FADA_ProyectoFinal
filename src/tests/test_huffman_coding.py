import unittest
from src.Huffman_coding import HuffmanCoding

class HuffmanCodingTestCase(unittest.TestCase):
    def test_encode(self):
        hc = HuffmanCoding()
        cadena = "mi pasion es programar"
        encoded_string = hc.encode(cadena)
        tree = hc.get_Tree()
        print(tree)

        expected_encoded_string = "111110000101100011111001010100100001000011100010100101010110001100111100001"
        self.assertEqual(encoded_string, expected_encoded_string)

if __name__ == "__main__":
    unittest.main()
