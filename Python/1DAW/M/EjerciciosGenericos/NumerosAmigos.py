num1=220
num2=284


sum1=0
sum2=0
for i in range(1,num1):
    if num1%i==0:
        sum1+=i

for i in range(1,num2):
    if num2%i==0:
        sum2+=i

if sum1==num2 and sum2==num1:
    print("Los numeros son amigos")
else:
    print("Los numeros no son amigos")