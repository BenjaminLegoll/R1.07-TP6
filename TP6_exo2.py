#fonction ajouter
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst


#a)
lst1 = [0, 1, 2]

#b)
lst2 = ajouter_elt(lst1, len(lst1))

#c)
print("lst1 :", lst1)
print("   type =", type(lst1))
print("   id   =", id(lst1))

print("\nlst2 :", lst2)
print("   type =", type(lst2))
print("   id   =", id(lst2))
