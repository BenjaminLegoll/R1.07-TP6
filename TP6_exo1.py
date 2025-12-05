#a)
L1 = [0] * 3
print("a) Liste :", L1)
print("   Type de L1 :", type(L1))
print("   id(L1) :", id(L1))

#b)
print("\nb) Éléments de L1 :")
for element in L1:
    print("   valeur =", element, "| type =", type(element), "| id =", id(element))

#c)
L1[1] = L1[1] + 1
print("\nc) Après modification du 2e élément :")
print("   Liste :", L1)
print("   Type de L1 :", type(L1))
print("   id(L1) (inchangé) :", id(L1))

#d)
print("\nd) Identifiants des éléments après modification :")
for element in L1:
    print("   valeur =", element, "| id =", id(element))

#e)
ma_chaine = "machaine"
print("\ne) Chaîne :", ma_chaine)
print("   id(ma_chaine) :", id(ma_chaine))
print("   Type :", type(ma_chaine))

print("\n   Caractères de la chaîne :")
for c in ma_chaine:
    print("   caractère =", c, "| type =", type(c), "| id =", id(c))
