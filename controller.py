"""
FelipedelosH
2025

Enigma Machine BY LOKO v2.0
"""
from CLL import CircularLinkedList


class EnigmaMachine:
    def __init__(self, alphabet, secret):
        self.alphabet = alphabet
        self.rotations = [0, 0, 0]
        self.actuatorBar = [0, 0, 0]
        self.CLLAlphabet = CircularLinkedList()
        self.rotorA = CircularLinkedList()
        self.rotorB = CircularLinkedList()
        self.rotorC = CircularLinkedList()
        self._initMachine(secret)
        
    def _initMachine(self, secret):
        for x in self.alphabet:
            self.CLLAlphabet.addData(x)
        self._convertSecretInRotations(secret)
        self._setRotorConections()

    def _setRotorConections(self):
        self.rotorA.wipeData()
        self.rotorB.wipeData()
        self.rotorC.wipeData()
        _total_chars = self.CLLAlphabet.count()
        for i in range(0, _total_chars):
            r1_map = f"{self.CLLAlphabet.getData(i)}:{self.CLLAlphabet.getData(i+self.rotations[0])}"
            self.rotorA.addData(r1_map)
            r2_map = f"{self.CLLAlphabet.getData(i+self.rotations[0])}:{self.CLLAlphabet.getData(i+self.rotations[1])}"
            self.rotorB.addData(r2_map)
            r3_map = f"{self.CLLAlphabet.getData(i+self.rotations[1])}:{self.CLLAlphabet.getData(i+self.rotations[2])}"
            self.rotorC.addData(r3_map)

    def _convertSecretInRotations(self, secret):
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
            self.rotations[0] = rotations_a

            rotations_b = sum([v for i, v in enumerate(vals) if i % 2 == 0])
            rotations_b = rotations_b%_total_chars
            self.rotations[1] = rotations_b

            rotations_c = sum([v for i, v in enumerate(vals) if i % 2 != 0])
            rotations_c = rotations_c%_total_chars
            self.rotations[2] = rotations_c

    def encrypt(self, text):
        txt = ""
        for i in text:
            chr = str(i)
            isUpper = str(chr).isupper()

            if isUpper:
                chr = str(chr).lower()

            if chr not in self.alphabet:
                txt = txt + i
                continue
            
            if isUpper:
                txt = txt + str(self._getEncryptChar(chr)).upper()
            else:
                txt = txt + str(self._getEncryptChar(chr))
            self._actionActuatorBar()

        return txt
    
    """
    Error... No Search by map character... search by rotor positions
    BUG
    """
    def _getEncryptChar(self, chr):
        # Convert in array
        # Serach chr in pos
        # STEP BY STEP BY POSITION
        temp = self.rotorA.getDataByStrPattern(f"{chr}:")
        temp = str(temp).split(":")[-1]
        temp = self.rotorB.getDataByStrPattern(f"{temp}:")
        temp = str(temp).split(":")[-1]
        temp = self.rotorC.getDataByStrPattern(f"{temp}:")
        temp = str(temp).split(":")[-1]

        return temp
    
    def _actionActuatorBar(self):
        self.actuatorBar[0] = self.actuatorBar[0] + 1
        if self.actuatorBar[0] >= len(self.alphabet):
            self.actuatorBar[0] = 0
            self.actuatorBar[1] = self.actuatorBar[1] + 1

        if self.actuatorBar[1] >= len(self.alphabet):
            self.actuatorBar[1] = 0
            self.actuatorBar[2] = self.actuatorBar[2] + 1

        if self.actuatorBar[2] >= len(self.alphabet):
            self.actuatorBar[2] = 0
