
print("""bienvenue a ce programme pour calculer ta moyenne.
Appuie a n'importe que moment sur 'q' pour arreter le programme""")
nombre = input("combien de nottes tu vas mettre ?")
if nombre.isnumeric():
    timer = int(nombre)
    while timer != 0:
        saisie = input("donne une note sur 20")
        if saisie == "q":
            break
        else:
            note = int(saisie)
            timer -= 1
            print(list)
elif nombre == "q":
    print("ok finito")


print("""bienvenue a ce programme pour calculer ta moyenne.
Appuie a n'importe que moment sur 'q' pour arreter le programme""")

nombre 