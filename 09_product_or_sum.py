premier = int(input("insere un premier nombre entier: "))
deuxieme = int(input("insere un deuxieme nombre entier: "))

if premier*deuxieme < 1000:
    print(f"le résultat de {premier}*{deuxieme} est égale a {premier*deuxieme}")
else:
    print(f"le résultat de {premier}+{deuxieme} est égale a {premier+deuxieme}")