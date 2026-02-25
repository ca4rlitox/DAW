k=1
for i in range(1,8):
    if i % 2 != 0:
        print("-------------")
    if i %2==0:
        for j in range (1,14):
            if j == 1 or j == 5 or j == 9 or j == 13:
                print("|", end="")
            elif j == 3 or j == 7 or j == 11:
                print(k, end="")
                k+=1
            else:
                print(" ", end="")
        print()
k=1
movimiento=[]
while(k<10 and k%2!=0):
    for i in range(1, 8):
        if i % 2 != 0:
            print("-------------")
        if i % 2 == 0:
            for j in range(1, 14):
                if j == 1 or j == 5 or j == 9 or j == 13:
                    print("|", end="")
                elif j == 3 or j == 7 or j == 11:
                    print("x", end="")
                    k += 1
                else:
                    print(" ", end="")
            print()