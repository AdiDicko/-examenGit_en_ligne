#  < !—premiere ligne de jeu - >

import random

def jeu_devine_nombre():
    print("🎯 Bienvenue dans le jeu Devine le Nombre !")
    print("Je pense à un nombre entre 1 et 100...")

    nombre_secret = random.randint(1, 100)
    tentatives = 0

    while True:
        try:
            choix = int(input("👉 Entre un nombre : "))
            tentatives += 1

            if choix < nombre_secret:
                print("📉 Trop petit !")
            elif choix > nombre_secret:
                print("📈 Trop grand !")
            else:
                print(f"🎉 Bravo ! Tu as trouvé en {tentatives} tentatives.")
                break

        except ValueError:
            print("⚠️ Entre un nombre valide !")

# Lancer le jeu
jeu_devine_nombre()