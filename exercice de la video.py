import random

number_to_guess = random.randint(1, 1000)
print(number_to_guess)
guess = False
while guess != number_to_guess:
    guess = int(input("entrez un nombre entre 1 et 1000 "))
    if guess > number_to_guess:
        print("c'est moin")
    elif guess < number_to_guess:
        print("c'est plus")
print(f"bravo vous avez trouvés le nombre {number_to_guess}")