def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    print("id(lst) =", id(lst))
    return lst


#a)
print("Appel 1 :", ajouter_elt())

#b)
print("Appel 2 :", ajouter_elt())

def ajouter_carac(ch="abc", elt="d"):
    print("id(ch)  =", id(ch))
    print("id(elt) =", id(elt))
    return ch + elt


#d)
print("\nAppel 1 :", ajouter_carac())

#e)
print("Appel 2 :", ajouter_carac())
