import random

def comparer(nombre_secret, choix):
    if choix < nombre_secret:
        return "trop petit"
    elif choix > nombre_secret:
        return "trop grand"
    else:
        return "gagné"


def jeu_devine_nombre():
    print("🎯 Bienvenue dans le jeu Devine le Nombre !")
    print("Je pense à un nombre entre 1 et 100...")

    nombre_secret = random.randint(1, 100)
    tentatives = 0

    while True:
        try:
            choix = int(input("👉 Entre un nombre : "))
            tentatives += 1

            resultat = comparer(nombre_secret, choix)

            if resultat == "trop petit":
                print("📉 Trop petit !")
            elif resultat == "trop grand":
                print("📈 Trop grand !")
            else:
                print(f"🎉 Bravo ! Tu as trouvé en {tentatives} tentatives.")
                break

        except ValueError:
            print("⚠️ Entre un nombre valide !")


# IMPORTANT 👇 (bonne pratique)
if __name__ == "__main__":
    jeu_devine_nombre()