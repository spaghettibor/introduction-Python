import random

number_to_guess = random.randint(1, 1000)
print(number_to_guess)
guess = False
abandon = False
while guess != number_to_guess:
    instruction = input("essayez un nombre entre 1 et 1000 / pressez q pour abandonner ")
    if not instruction.isnumeric():
        if instruction == "q":
            abandon = True
            break
    guess = int(instruction)
    if guess > number_to_guess:
        print("c'est moin")
    elif guess < number_to_guess:
        print("c'est plus")

if abandon == True:
    print(f"dommage le nombre était {number_to_guess}")
else:
    print(f"bravo vous avez trouvés le nombre {number_to_guess}")