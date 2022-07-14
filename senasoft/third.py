numbers=[]
i=1
while i<=20:
    number=int(input("Enter a number: "))
    if number<100:
        numbers.append(number)
    else:
        print("The number is too big")
    i+=1

print(numbers)