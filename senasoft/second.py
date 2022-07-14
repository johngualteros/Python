number=int(input("Enter a number: "))
acumulator=0
count=0
storeNumbers=[]

while number>0:
    storeNumbers.append(number)
    acumulator+=number
    count=count+1
    number=int(input("Enter a number: "))

average=acumulator/count
print(storeNumbers)
print("The average is {}".format(average))

