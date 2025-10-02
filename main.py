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
enigma = EnigmaMachine(alphabeth)
print(f"TOTAL data in EM: {enigma.alphabet.count()}")

text = "Hola Mundo Yo Soy Molotov y este es mi texto encriptado."
