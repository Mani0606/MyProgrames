import random
ranNumber = random.randint(1,10)
GusNumber = 0
print("You have Seven Chances")
while(GusNumber != ranNumber):
    for i in range(1,8):
        print(f"{i} chance")
        GusNumber = int(input("Guess The Number: "))
        if GusNumber==ranNumber:
            print("It's Matched")
            break
        elif GusNumber != ranNumber:
            if GusNumber>ranNumber:
                print(f"{GusNumber} is higher")
            elif GusNumber<ranNumber:
                print(f"{GusNumber} is Lower")
    break
