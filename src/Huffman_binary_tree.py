"""
Proyecto final: FADA algoritmo Huffman

Integrantes y autores:
    2067805 Andres Mauricio Arias Cortes
     Santiago Marin Lozano
     Maher Lopez Rodriguez


Este modulo contiene la clase HuffmanBinaryTree


"""

class HuffmanBinaryTree:
    """
    Clase que representa un arbol binario de Huffman
    """

    def __init__(self, character=None, frequency=0):
        """
        Init de la clase HuffmanBinaryTree
        """
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def is_leaf(self):
        """
        Metodo que verifica si el nodo es una hoja
        """
        return self.left is None and self.right is None
