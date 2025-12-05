s = input("Mot ou phrase : ")
s2 = ""
for c in s:
    if c.isalpha():
        s2 += c.lower()

if s2 == s2[::-1]:
    print("Palindrome !")
else:
    print("Pas palindrome")
