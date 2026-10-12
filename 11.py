
print("""bienvenue a ce programme pour calculer ta moyenne.
Appuie a n'importe que moment sur 'q' pour arreter le programme""")

termine = 0
nombre = 0
valeur = 0
somme = 0
while termine == 1:
    valeur = input("donne un nombre et si tu as fini alors dis finito ")
    if valeur.isnumeric():
        valeur_int = int(valeur)
        somme += valeur_int
        nombre += 1
    if valeur == "q":
        break
    elif valeur == "finito":
        termine == 0
print(f"la moyenne est égale a {somme/nombre}")
    