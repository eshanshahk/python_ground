num=int(input(""))
a=num*num
sumOfDigit=0

while num>0:
    digit=a%10
    sumOfDigit=+digit
    a=a//10

if(sumOfDigit==num):
    print("Neon Number")
else:
    print("Not a Neon Number")
