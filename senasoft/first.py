numberStart=int(input("Enter a number: "))
numberEnd=int(input("Enter a number: "))
acumulatorOdd=0
acumulatorEven=0

for i in range(numberStart, numberEnd+1):
    if i%2==0:
        acumulatorEven+=i
    elif i%2!=0:
        acumulatorOdd+=i

diference=acumulatorEven-acumulatorOdd
print("The sum with even is {} and  the sum with odd is {}".format(acumulatorEven, acumulatorOdd))
print("The difference is {}".format(diference))