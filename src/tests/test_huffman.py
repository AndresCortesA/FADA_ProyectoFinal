from src.Huffman_coding import HuffmanCoding
from src.Huffman_decoding import HuffmanDecoding


def test_huffman_coding():
    # Crear una instancia de la clase HuffmanCoding
    huffman = HuffmanCoding()

    # Codificar una cadena de texto
    cadena = "mi pasion es programar 20"
    encoded_string = huffman.encode(cadena)

    # Decodificar la cadena codificada
    huffman_decoding = HuffmanDecoding()
    huffman_decoding.tree = huffman.tree
    decoded_string = huffman_decoding.decode(encoded_string)

    # Guardar los datos codificados en un archivo
    filename = "encoded_data.bin"
    huffman.write_encoded_data_to_file(filename, encoded_string)

    # Leer los datos codificados desde el archivo
    encoded_data = huffman.read_encoded_data_from_file(filename)

    # Obtener el árbol de Huffman
    huffman_tree = huffman.get_Tree()

    # Obtener la tabla de Huffman
    huffman_table = huffman.get_Table()

    # Obtener un resumen de la compresión
    summary = huffman.get_Summary(cadena)

    # Guardar los prints en un archivo
    with open("output.txt", "w") as file:
        file.write("Cadena codificada: {}\n".format(encoded_string))
        file.write("Cadena decodificada: {}\n".format(decoded_string))
        file.write("Datos codificados leidos desde el archivo: {}\n".format(encoded_data))
        file.write("Arbol de Huffman: {}\n".format(huffman_tree))
        file.write("Tabla de Huffman: {}\n".format(huffman_table))
        file.write("Resumen de la compresion: {}\n".format(summary))

# Ejecutar la función de prueba
test_huffman_coding()
