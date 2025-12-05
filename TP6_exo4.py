import random

def generer(nbr, vmin, vmax):
    table = []
    for _ in range(nbr):
        table.append(random.randint(vmin, vmax))
    return table

def combienInferieur(table, vseuil):
    compteur = 0
    for valeur in table:
        if valeur < vseuil:
            compteur += 1
    return compteur

nb = int(input("Combien de valeurs voulez-vous générer ? "))
vmin = int(input("Valeur minimale (vmin) : "))
vmax = int(input("Valeur maximale (vmax) : "))

print(f"\nGénérer {nb} nombres entiers entre {vmin} et {vmax}")

tab = generer(nb, vmin, vmax)
tab.sort()

print("\nTableau généré :")
print(tab)
