import time
print("Compte à rebours !")
number = 10
while number > 0:
    print(number)
    time.sleep(1)
    number -= 1
print("Boom !")