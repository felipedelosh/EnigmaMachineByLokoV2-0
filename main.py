"""
FelipedelosH
2025

Encryptor By Loko
"""
from controller import EnigmaMachine


_env = ""
with open(".env", "r", encoding="UTF-8") as f:
    _env = f.read()


print("========= WELCOME TO ENIGMA MACHINE BY LOKO V2.0 ==========")
print(f"ENV->\n{_env}")
alphabeth = _env.split("\n")[0].split("=")[-1]
secret = _env.split("\n")[1].split("=")[-1]
enigma = EnigmaMachine(alphabeth, secret)
print(f"TOTAL data in EM: {enigma.CLLAlphabet.count()}")
print(f"Rotations by secret: {enigma._convertSecretInRotations(secret)}")
print(f"Rotor A DATA: {[(i, x) for i, x in enumerate(enigma.rotorA.converDataInArray())]}")
print("=================================")
print(f"Rotor B DATA: {[(i, x) for i, x in enumerate(enigma.rotorB.converDataInArray())]}")
print("=================================")
print(f"Rotor C DATA: {[(i, x) for i, x in enumerate(enigma.rotorC.converDataInArray())]}")
print("=================================")
text = "Hola Mundo Yo Soy Molotov y este es mi texto encriptado... desde el 2025 :)"
print(f"TEXT:\n{text}")
encryptTXT = enigma.encrypt(text)
print(f"Encrypt:\n{encryptTXT}")
print("=================================")
decryptTXT = enigma.encrypt(encryptTXT)
print(f"Decrypt:\n{decryptTXT}")
