"""
FelipedelosH
2025

Enigma Machine BY LOKO v2.0
"""
from CLL import CircularLinkedList


class EnigmaMachine:
    def __init__(self, alphabet):
        self.alphabet = CircularLinkedList(x for x in alphabet)
        self.rotorA = None
        self.rotorB = None
        self.rotorC = None
        

    def initRotors(self):
        pass
