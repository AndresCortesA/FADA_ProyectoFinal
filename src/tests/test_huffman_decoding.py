import unittest
from src.Huffman_coding import HuffmanCoding
from src.Huffman_decoding import HuffmanDecoding

class HuffmanCodingTestCase(unittest.TestCase):
    def test_encode_decode(self):
        huffman_coding = HuffmanCoding()

        # Datos de prueba
        cadena_original = "mi pasion es programar"

        # Codificar la cadena original
        cadena_codificada = huffman_coding.encode(cadena_original)

        # Decodificar la cadena codificada
        huffman_decoding = HuffmanDecoding()
        huffman_decoding.tree = huffman_coding.tree
        cadena_decodificada = huffman_decoding.decode(cadena_codificada)

        # Verificar el resultado
        self.assertEqual(cadena_decodificada, cadena_original)
        

if __name__ == '__main__':
    unittest.main()
