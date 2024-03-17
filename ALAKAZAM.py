import sys
import hashlib
import os
import colorama
from colorama import Fore,Style
import argparse


def calcul_longueur_hash(hash):
    return len(hash)

def verif_hash(chaine):
    for char in chaine:
        if not ((char >= '0' and char <= '9') or (char >= 'a' and char <= 'f') or (char >= 'A' and char <= 'F')):
            return False
    return True

def analyse_hash(hash):
    longueur_hash = calcul_longueur_hash(hash)

    if longueur_hash == 32:
        # MD5 hash
        return 1
    elif longueur_hash == 40:
        # SHA-1 hash
        return 2
    elif longueur_hash == 64:
        # SHA-256 hash
        return 3
    elif longueur_hash == 128:
        # SHA-512 hash
        return 4
    elif longueur_hash == 56:
        # SHA3-224 hash
        return 5
    elif longueur_hash == 96:
        # SHA3-384 hash
        return 6

    return 0

def print_hash_type(type):
    hash_types = {
        1: "Le hash saisie est surement un hash MD5",
        2: "Le hash saisie est surement un hash SHA-1",
        3: "Le hash saisie est surement un hash SHA-256",
        4: "Le hash saisie est surement un hash SHA-512",
        5: "Le hash saisie est surement un hash SHA3-224",
        6: "Le hash saisie est surement un hash SHA3-384",
    }

    print(hash_types.get(type, "Type de Hash pas encore implanté ou inconforme"))

def analyse_fichier(chemin_fichier):
    try:
        with open(chemin_fichier, 'r') as fichier:
            for ligne in fichier:
                hashes = ligne.strip().split(';')
                for h in hashes:
                    hash_type = analyse_hash(h)
                    if hash_type != 0:
                        print(f"{h}: ", end='')
                        print_hash_type(hash_type)
                    else:
                        print(f"{h}: Invalid hash")
    except FileNotFoundError:
        print(f"Erreur lors de l'ouverture du fichier {chemin_fichier}")
        return 1

    return 0

def main():
    if len(sys.argv) == 0:
        None

    else : 
        os.system("cls" if os.name == "nt" else "clear")
        print_ascii_art()

    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print("Ce programme en Python permet d'analyser un hash et de renvoyer de quel type de hash il s'agit parmi cette liste :")
        print("MD5")
        print("SHA-1")
        print("SHA-256")
        print("SHA-512")
        print("SHA3-224")
        print("SHA3-384")
        print("Options:")
        print("  -h <hash>   : Entrez le hash a analyser")
        print("  -f <chemin/du/fichier> : Specifiez un fichier contenant des hashes separes par des ';'")
        print("  -help        : Afficher ce message d'aide")
        return 0
    elif len(sys.argv) == 3 and sys.argv[1] == '-h':
        hash_type = analyse_hash(sys.argv[2])
        if hash_type != 0:
            print_hash_type(hash_type)
        else:
            print("Invalide hash")
        return 0
    elif len(sys.argv) == 3 and sys.argv[1] == '-f':
        return analyse_fichier(sys.argv[2])
    else:
        return 1
    

def print_ascii_art():
    print(Fore.LIGHTBLUE_EX +'''
          
 ▄▄▄       ██▓    ▄▄▄       ██ ▄█▀▄▄▄      ▒███████▒ ▄▄▄       ███▄ ▄███▓
▒████▄    ▓██▒   ▒████▄     ██▄█▒▒████▄    ▒ ▒ ▒ ▄▀░▒████▄    ▓██▒▀█▀ ██▒
▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓███▄░▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██  ▀█▄  ▓██    ▓██░
░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▓██ █▄░██▄▄▄▄██   ▄▀▒   ░░██▄▄▄▄██ ▒██    ▒██ 
 ▓█   ▓██▒░██████▒▓█   ▓██▒▒██▒ █▄▓█   ▓██▒▒███████▒ ▓█   ▓██▒▒██▒   ░██▒
 ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▒ ▓▒▒▒   ▓▒█░░▒▒ ▓░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░
  ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒ ▒░ ▒   ▒▒ ░░░▒ ▒ ░ ▒  ▒   ▒▒ ░░  ░      ░
  ░   ▒     ░ ░    ░   ▒   ░ ░░ ░  ░   ▒   ░ ░ ░ ░ ░  ░   ▒   ░      ░   
      ░  ░    ░  ░     ░  ░░  ░        ░  ░  ░ ░          ░  ░       ░   
                                           ░                             
author : flem
github : https://github.com/FL3MM3
______________________________________________
'''.strip() + Style.RESET_ALL)

if __name__ == "__main__":
    sys.exit(main())
