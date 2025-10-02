"""
FelipedelosH
2025

Enigma Machine BY LOKO v2.0
"""
from CLL import CircularLinkedList


class EnigmaMachine:
    def __init__(self, alphabet, secret):
        self.alphabet = CircularLinkedList()
        self.rotorA = CircularLinkedList()
        self.rotorB = CircularLinkedList()
        self.rotorC = CircularLinkedList()
        self.initMachine(alphabet, secret)
        
    def initMachine(self, alphabet, secret):
        for x in alphabet:
            self.alphabet.addData(x)
        _mixed = self.convertSecretInRotations(secret)
        _total_chars = self.alphabet.count()
        for i in range(0, _total_chars):
            r1_map = f"{self.alphabet.getData(i)}:{self.alphabet.getData(i+_mixed[0])}"
            self.rotorA.addData(r1_map)
            r2_map = f"{self.alphabet.getData(i+_mixed[0])}:{self.alphabet.getData(i+_mixed[1])}"
            self.rotorB.addData(r2_map)
            r3_map = f"{self.alphabet.getData(i+_mixed[1])}:{self.alphabet.getData(i+_mixed[2])}"
            self.rotorC.addData(r3_map)

    def convertSecretInRotations(self, secret):
        result = [0, 0, 0]
        _total_chars = self.alphabet.count()
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
