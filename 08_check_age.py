naissance = int(input("donne ton annee de naissance stp"))
age = 2026 - naissance

if age <= 12:
    type = "enfant"
elif age > 12 and age < 18:
    type = "ado"
else:
    type = "adulte"


print(f"a la fin de l'annee 2026 tu auras {age} ans et tu es un {type}")