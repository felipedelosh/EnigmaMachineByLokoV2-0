"""
FelipedelosH
2025

Enigma Machine BY LOKO v2.0
"""
from CLL import CircularLinkedList


class EnigmaMachine:
    def __init__(self, alphabet, secret):
        self.alphabet = alphabet
        self.CLLAlphabet = CircularLinkedList()
        self.rotorA = CircularLinkedList()
        self.rotorB = CircularLinkedList()
        self.rotorC = CircularLinkedList()
        self._initMachine(secret)
        
    def _initMachine(self, secret):
        for x in self.alphabet:
            self.CLLAlphabet.addData(x)
        _mixed = self._convertSecretInRotations(secret)
        _total_chars = self.CLLAlphabet.count()
        for i in range(0, _total_chars):
            r1_map = f"{self.CLLAlphabet.getData(i)}:{self.CLLAlphabet.getData(i+_mixed[0])}"
            self.rotorA.addData(r1_map)
            r2_map = f"{self.CLLAlphabet.getData(i+_mixed[0])}:{self.CLLAlphabet.getData(i+_mixed[1])}"
            self.rotorB.addData(r2_map)
            r3_map = f"{self.CLLAlphabet.getData(i+_mixed[1])}:{self.CLLAlphabet.getData(i+_mixed[2])}"
            self.rotorC.addData(r3_map)

    def _convertSecretInRotations(self, secret):
        result = [0, 0, 0]
        _total_chars = self.CLLAlphabet.count()
        s = str(secret).lower()
        vals = []
        first_seen = {}
        next_id = 1
        for ch in s:
            if ch not in first_seen:
                first_seen[ch] = next_id
                next_id += 1
            vals.append(first_seen[ch])

        if vals:
            rotations_a = sum(vals)
            rotations_a = rotations_a%_total_chars
            result[0] = rotations_a

            rotations_b = sum([v for i, v in enumerate(vals) if i % 2 == 0])
            rotations_b = rotations_b%_total_chars
            result[1] = rotations_b

            rotations_c = sum([v for i, v in enumerate(vals) if i % 2 != 0])
            rotations_c = rotations_c%_total_chars
            result[2] = rotations_c
        
        return result
    

    def encrypt(self, text):
        txt = ""
        for i in text:
            if i not in "":
                continue


        return txt
