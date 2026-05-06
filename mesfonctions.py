# < !—premiere ligne -- >

def addition(a, b):
    return a + b

def est_pair(n):
    return n % 2 == 0

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

def inverser_chaine(texte):
    return texte[::-1]

def compter_voyelles(texte):
    voyelles = "aeiouyAEIOUY"
    return sum(1 for lettre in texte if lettre in voyelles)

def trouver_max(liste):
    return max(liste)

def trier_liste(liste):
    return sorted(liste)

def celsius_vers_fahrenheit(c):
    return (c * 9/5) + 32

def est_palindrome(mot):
    return mot == mot[::-1]

def generer_pairs(n):
    return [i for i in range(n) if i % 2 == 0]

# test unitaire 1
print(addition(2, 3))

#test unitaire 2
print(est_pair(4))

#test unitaire 3
print(factorielle(5))

#test unitaire 4
print(inverser_chaine("Bonne soirée monsieur"))

#test unitaire 5
print(est_palindrome("kayak"))