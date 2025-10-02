"""
FelipedelosH
2025

Enigma Machine BY LOKO v2.0
"""
from CLL import CircularLinkedList


class EnigmaMachine:
    def __init__(self, alphabet):
        self.alphabet = CircularLinkedList()
        self.rotorA = CircularLinkedList()
        self.rotorB = CircularLinkedList()
        self.rotorC = CircularLinkedList()
        self.initMachine(alphabet)
        
    def initMachine(self, alphabet):
        for x in alphabet:
            self.alphabet.addData(x)
