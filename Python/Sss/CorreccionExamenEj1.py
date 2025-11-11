import random

for _ in range(0,4):
    for i in range(0,5):
        for _ in range(0,5):
            print(random.randint(0, 9), end="")
            if i!=4:
                print("-", end="")
            else:
                print("")