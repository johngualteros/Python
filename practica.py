# print("hello world")
# print (2**5) exponenciacion.
# print(9**(1/2))

# Declaramos Las Variables
# dayInHours=24
# hourInMinutes=60
# minuteInSeconds=60
# # Creamos la funcionalidad
# resultDayInSeconds= (dayInHours*hourInMinutes)*minuteInSeconds
# resultDayIn30Days=resultDayInSeconds*30
# print("30 days have "+ str(resultDayIn30Days)+" in seconds")


# Calcular numero de bacterias

# startBacteries=500
# multiplicityPerHour=2
# day=24
# print(startBacteries*multiplicityPerHour**day)

# print(20//6) este calculara el cociente pero siempre traera el numero entero
# print(20%6) este traera el resiudo de la division en este caso el numero 2

# calcular las horas a partir de minutos
# hour=60
# hours=888//hour
# minutesRestant=888%hour
# print(str(hours)+" Hours")
# print(str(minutesRestant)+" Minutes")

# Calcular el tiempo de vuelo de un avion en N cantidad de millas en horas
# speedPerMileInOneHour=550
# time=7425/speedPerMileInOneHour

# print(time)

# poner comillas al texto sin romper a python
# print('Hello world\'')

# print('\"Stay hungry, stary foolish\"by Steve jobs')

# # Poner un string con salto de linea \n
# print(' one \n two \n three \n four \n five')
# Otra forma de hacerlo """
# print("""This
# is a
# multiline
# text""")

# Concatenacion
# name='John'
# print('Hello '+name)
# Imprimira el mensaje 10 veces en lineas distintas
# print('You\'re stupid\n'*10)

# proyecto modulo 2 python for beginners
# initial=1
# for initial in range(1,10):print(str(initial)+'.')

# print(' 1.\n 2.\n 3.\n 4.\n 5.\n 6.\n 7.\n 8.\n 9.')
# print("""1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.
# """)

# Variables 
# name='john'
# print(name*5)

# name='John Gualteros'
# age=17
# print('name is '+name+' age years old '+str(age) )

# Metodo de entradas
# name=input("Enter your name: ")
# print("hello "+name)

# # Recibir entrada de tipo entero
# age=int(input("Enter your age "))
# print('age is '+str(age))
# print('name is: '+name+ ' and age is'+ str(age))

# Acumulador 
# number1=13
# number1+=number1*3
# # Is the same with the strings
# print(number1)
# spam='7'
# spam+='3'
# # 70
# eggs=int(spam)+3
# # 73
# print(float(eggs))
# 73.0

# Examen calculadora de propinas
# propine=int(input('por favor digite el total de la factura: '))
# porcentage=propine*20/100
# print(float(porcentage))

# Booleans and if
# my_boolean=True
# print(my_boolean)

# print(2 == 4)
# print('hello' == 'hello')

# exampleNull='hello'
# print(exampleNull!='')

# Condiciones if
# numero1=8
# # if numero1<=9 : print(True)
# # if anidados
# number1=13
# # if number1>=10:
# #     print("true")
# #     if number1<=20:print("true")
# # else
# number2=9
# if number2==9:print(True)
# else: print(False)

# example=5
# if example==2:
#     print("two")
# else:
#     if example==4:
#         print("four")
#     else:
#         if example==5:
#             print("five") 

# example2=100
# if example2==50:
#     print("50 yes")
# elif example2==100:
#     print("100 yes")

# if con 2 condiciones
# print(2==2 and 'dani'=='dani')
# print(1+1==2 and 'john'=='dani')
# print(180//60==3 and 2**5!=20) # is the same with (or) || example {if number1==2 or number1!=10:print(True)}

# # the operator (not) is the reverse  True is False and False is True
# print(not 1==1)
# print(not 2!=2) #in if the example is if not True:print("1")

# Bucles while
# i=1
# while i<=13:
#     print(i)
#     i+=1
# print('Finished')

# x=1
# while x<=10:
#     if x%2==0:
#         print(str(x)+' par')
#     else:
#         print(str(x)+' inpar')
#     x+=1
# print('Finished')
# Break

# No se cual es el error
# i=0
# while 1==1:
#     i=i+1
#     if i >= 51:
#         print(i)
#         print('breaking')
#     break
# print('breaking2')
# print('Finished')
# i=0
# while i<5:
#     i+=1
#     if i==3:
#         print('Skipping 3')
#         continue
#     print(i)

# i=0
# x=0
# while i<4:
#     x+=i #[1,3,6]
#     i+=1 #[1,2,3,4]
# print(x)

# Calculadora de IMC Solo learn practices

# heigth=float(input('Please enter your heigth'))
# weight=float(input('Please enter your weight'))

# saludable=weight//heigth**2

# if saludable <18.5:
#     print('Underweigth')
# elif saludable>=18.5 and saludable<24.9:
#     print('Normal')
# elif saludable>=25 and saludable<29.9:
#     print('Overweigth')
# elif saludable>=30:
    # print('Obesity')
#Lists
# words=['hello', 'world', '!']
# print(words[0])
# print(words[1])
# print(words[2])

# matriz=[[1,2,3],[4,5,6]]
# print(matriz[1][2])

# strings with list 
# string='Hello World!'
# print(string[6])
# # operations with list 
# numbers=[1,2,3]
# numbers2=[1,2,4]
# print(numbers+numbers2)
# print(numbers*3)

# x=[2,4]
# x+=[6,8]
# print(x[2]//x[0])
# Para comprobar si un elemnto esta en una lista podemos usar (in)
# words=['eggs','milk','spam','spam']
# print('spam' in words)
# print('tomato' in words)
# print(not 'tomato' in words)
# print(not 'eggs' in words)
# if 'eggs' in words:
#     print('yes')
# Cycle for
# letters=['t','e','a','m','o']
# for letter in letters:
#     print(letter+'!')

# string='Hola mi nombre es john alejandro gualteros garcia'
# start=input('Please enter yout letter for want: ')
# count=0

# for x in string:
#     if(x==start):
#         count+=1
# print(start+' : '+str(count))


# # Rangos
# number=list(range(1,11))
# print(number)
# Range with 3 arguments and it is step
# numbers=list(range(0,21,2))
# print(numbers)

# for i in range(11):
#     print('Hello world')
# # Sacar listas de un indice a otros
# listOfNumbers =[1,2,4,5,7,5,4,3,2,9,212,43,343,6,763,4,55]
# # print(listOfNumbers[2:10])#only copy the array
# # print(listOfNumbers)
# # si no se la pasa parametro lo tomara desde el principio o hasta el final
# # print(listOfNumbers[:11])
# # print(listOfNumbers[10:])
# # print(listOfNumbers[::2])
# print(listOfNumbers[2:9:3])#el primero es normal despues llegara hasta el indice del 
# #segundo y el tercero seran los espacios que saltara pero empieza desde 180
# print(listOfNumbers[1::4])#2596 se empezara desde el indice 1 hasta el 4 a partir del primer indice
# # despues saltara 4 posiciones desde el numero hasta terminar el arreglo

# # los valores negativos haran que empiece de atras para adelante el
# print(listOfNumbers[1:-1])
# print(listOfNumbers[3:-3])
# print(listOfNumbers[7:5:-1])#9-5 salta de 1
# x=[6,4,2,9]
# x=x[::-1]
# print(x[0]+x[2])

# Project module 5
# numberEnterWithPerson=int(input('Please enter one number: '))
# acumulator=0
# for i in range(1,numberEnterWithPerson+1):
#    acumulator+=i

# print(acumulator)

# Function in python 

# print(range(0,100,5))#argumentos en este caso 3

# nums=[1,2,3,4,5,6,7,8,8,5,132,65,4,5,432,75,4,34,3,3334]

# print(len(nums))#devolvera el numero de indices que hay en este caso 20 empieza desde 1

# numbers=[1,2,3,4]
# numbers.append(10)#agregara un nuevo valor al final
# print(numbers)

# words=['firefox', 'chrome']
# index=int(input('Please enter the index in you want insert the value '))
# wordEnterForTheUser=input('Please enter the word you want insert in the array ')
# words.insert(index, wordEnterForTheUser) #Inserta elementos a un arreglo
# print(words)

# encontrara el primer indice
# letters=['a', 'b', 'c', 'd', 'e','f']
# print(letters.index('a'))
# print(letters.index('c'))
# print(letters.index('f'))
# print(letters.index('e'))

# numbers=[1,3,45,6,7,7,5,5,7,34,54,4,65,433,455,576,4,56,35,4,343453,121,453,34,2,2,1,12,4,5,3,2,4]
# # max(list) numero mayor
# print(max(numbers))
# # min(list) numero menor
# print(min(numbers))
# # count(item) recuento de cuantas veces esta el numero o string
# print(numbers.count(7))
# print(numbers.count(2))
# # remove(item) elimina el elemento de la lista 
# print(numbers.remove(7))
# print(numbers.remove(7))
# print(numbers.remove(7))
# print(numbers)
# # reverse invierte los valores de una lista 
# numbers.reverse()
# print(numbers)


# # Formatt in strings
# # function format
# nums=[1,2,3,5]
# message="Numbers: {3} {1} {0} {2}".format(nums[3],nums[1],nums[0],nums[2])
# print(message)

# a="{x} {y}".format(x=5, y=12)
# print(a)

# Create my functions
# def printHelloWorld():
#     print("Hello World!")

# printHelloWorld()
# printHelloWorld()

# # Function with arguments 
# def myWordPrint(word):
#     print(word+'!!')

# myWordPrint('John')
# myWordPrint('John2')
# myWordPrint('John3')

# def suma(number=0,number2=0):
#     print(number+number2)

# suma(2,10)
# suma(10)
# suma(0,15)

# def max(firstNumber,secondNumber):
#     if firstNumber > secondNumber:
#         return firstNumber
#     else:
#         return secondNumber

# print(max(2,56))
# maxNumber=max(10,11)
# print(maxNumber)

# def division(firstNumber,secondNumber):
#     total=firstNumber//secondNumber
#     return total
#     print('ready this not print')#all after in return not are print

# print(division(180,5))

# # DocStrings

# def docString(word):
#     """
#     This to is one comment but it is ejecuted
#     """
#     print(word+'!')

# docString('Python')

"""this is the final module for get the certification python for begginners"""

# from itertools import count


# phrase = input('Please entre the phrase: ')
# word=input('Please enter the word: ')

# def search(phrase,word):
#     print(phrase.split(' '))
#     if phrase.count(word):
#         print('word found')
#     else:
#         print('word not found')
# search(phrase,word)


"""Intermediate Python Course"""

"""Dictionarys"""
# import numbers


# words=['hi','hello','welcome']
# print(words[0])

# ages={
#     'davy':20,
#     'luis':23,
#     'carlos':47
# }

# # print(ages['davy'])

# numbersInLetters={
#     [0,1,2,3]:'zero one two three'
#}it present error with only can put 1 key

"""Example dictionary in one car"""
# car={
#     'brand':'bmw',
#     'year':2018,
#     'color':'red'
# }

"""Comprobate if one key or value is include in the dictionary"""
# nums={
#     1:'one',
#     2:'two',
#     3:'three'
# }

# print(1 in nums)
# print('three' in nums)
# print(4 not in nums)

"""Si no encuentra el index traera el segundo argumento despues de la coma"""
# pairs={
#     1:"pineapple",
#     'orange':[1,2,3,4],
#     True:False,
#     12:'True'
# }
# print(pairs.get('orange'))
# print(pairs.get(13, 0))
# print(pairs.get(2012, 'Not found in the dictionary'))

"""TUPLA This type with parhentesis is not mutable or can be used sin parhentesis"""

# words=('eggs', 'beer' ,'milk')

# print(words[1])

"""se puede asignar elementos de una tupla"""
# numbers=(1,2,3)

# a,b,c=numbers
# print(a)
# print(b)
# print(c)

"""con el * tomara todos los elementos restantes de las varibales"""

# import numbers


# a,b,c,*d=(1,2,3,4,5,5,32,7,7,6,4,4,3,2,34,5,7,7,4,4,4,3,23,3,3234)
# print(str(a)+'\n'+str(b)+'\n'+str(c)+'\n'+str(d))

"""comprobar si un elemento existe"""

# number={1,2,3,4}
# print(3 in number)

"""add y remove para agregar elementos a conjuntos"""

# numbers={1,2,3,4,5,6,7,8,9}
# print(numbers)
# numbers.add(-7)
# numbers.remove(7)
# print(numbers)
# print(len(numbers))
# list1={1,2,3,4,5}
# list2={6,7,8,9,1,2,3}
"""union | combina 2 conjuntos"""
# print(list1|list2)
"""interseccion & obtiene elementos solo en ambos"""
# print(list1&list2)
"""diferencia - obtiene elementos solo en el primero"""
# print(list1-list2)
# print(list2-list1)
"""diferencia simetrica ^ obtiene elementos en cualquiera pero no en ambos"""
# print(list1^list2)

"""La comprension de listas"""

"""calculate the cube in the number digitate"""

# number=int(input('Please enter the number you want calculate the cube: '))
# initial=1

# def calculatorCube(number, initial):
#     cubesNumbers=[i**3 for i in range(initial,number+1)]
#     print(cubesNumbers)

# calculatorCube(number,initial

# )

"""calcular la raiz cuadrada pares y impares aparte"""

# number=int(input('Please enter the number: '))

# def calcularRaizCuadrada(number):
#     pares=[i*i for i in range(number+1) if i**i %2==0]
#     inpares=[i*i for i in range(number+1) if i**i %2!=0]
#     print('pares: '+str(pares))
#     print ('inpares: '+str(inpares))

# calcularRaizCuadrada(number)

"""first module python intermediate"""
#first Solution
# text=input('Please enter the text: ')
# dictionary={}

# for letter in text:
#     if letter in dictionary:
#         dictionary[letter]+=1
#     else:
#         dictionary[letter]=1
    

# print(dictionary)

"""Programation funtional"""

# def firstFunction(function,argument):
#     return function(function(function(argument)))

# def sumar5(number):
#     return number+5

# print(firstFunction(sumar5,10))

"""Function pure"""

# def pureFunction(number1,number2):
#     temp= number1+2*number2
#     return temp/(2*number1+number2)

"""Function inpure"""
# someList=[]
# def inpureFunction(argument):
#     someList.append(argument)
#     print(someList)

# inpureFunction('Hello world')

"""comprobar si es palindromo"""
# word = input("please enter the text: ")#capturamos el texto digitado por el usuario
# if str(word) == str(word)[::-1] : #if donde comparamos el texto normal y a la reversa el conjunto [::-1] sirve para darle reversa al string
#     print("Palindrome")
# else:
#     print("Not Palindrome")

"""Lambdas"""
# def myfunction(number,arguments):
#     return number(arguments)

# print(myfunction(lambda x:2*x*x,5))


# def polynomial(x):
#     return x**2 +5*x +4
# # print (polynomial(-4))
# print((lambda x:x**2 +5*x +4)(-4))




# number=int(input("Please enter the number in with you want to generate the raise square: "))

# def CalculatorRaiceSquare(number):
#     pares=[i*i for i in range(number+1) if i**i %2==0]
    
#     inpares=[i*i for i in range(number+1) if i**i %2!=0]

#     print(pares)
#     print(inpares)

# CalculatorRaiceSquare(number)
"""Map"""
# number=int(input("Please enter the number: "))

# def addNumber(x):
#     return x+number

# nums=[11,22,33,44,55,66,77,88,99,111]
# result=list(map(addNumber,nums))
# print(result)

"""Filter"""

# def filterFunction(x):
#     return x<=5
# nums=1,2,3,4,5,6,7,8,9,10,11,12
# print(list(filter(filterFunction,nums)))

# #other Example

# numbers=[11,22,33,44,55,66,77,88,99,111]
# print(list(filter(lambda x:x%2!=0,numbers)))

"""Exercise entrevista"""

#retornar las 3 primeras palabras de una lista 

# words="Hello world this is one example for the exercise"
# def Result(words):
#     splited=words.split()
#     return print(splited[:3])

# Result(words)

"""Generadores yield"""
# def countdown():
#     i=5
#     while i>0:
#         yield i
#         i-=1

# for i in countdown():
#     print(i)

# from time import sleep


# def infinite_numbers():
#     i=1
#     while True:
#         yield i
#         i+=1
#         sleep(1)

# for i in infinite_numbers():
#     print(i)


# def numbers(x):
#     for i in range(x):
#         if i%2==0:
#             yield i

# print(list(numbers(11)))
# from time import sleep


# def printDownload():
#     i=0
#     while i<=100:
#         yield i
#         i+=1
#         if i>=20:
#             sleep(0.1)
#         else:
#             sleep(0.4)

# for i in printDownload():
#     print('tu descarga va en: ',str(i));


"""decoradores"""
# def decor(func):
#     def wrap():
#         print("=========")
#         func()
#         print("=========")
#     return wrap
# @decor
# def print_text():
#     print("Hello World!!")

# print_text()


#decorator exercise 
# def decorate(function):
#     def wrap(num):
#         print("***")
#         function(num)
#         print("***")
#         print("END OF PAGE")
#     return wrap
# @decorate
# def invoice(num):
#     print("INVOICE #"+num)

# invoice(input());

"""Recursividad"""
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return  x*factorial(x-1)

# print(factorial(5))

# def is_even(x):
#     if x==0:
#         return True
#     else:
#         return is_odd(x-1)

# def is_odd(x):
#     return  not is_even(x)

# print(is_odd(17))
# print(is_even(23))

"""Args"""
# def function(named_arg,*arg):
#     print(named_arg)
#     print(arg)
# function(1,2,3,4,5)
# def function(x,y=7,*args,**kwargs):
#     print(kwargs)

# function(2,3,4,5,6,a=7,b=8)

"""First Module in Solo learn python for intermediate"""
# def spell(txt):
#     reverser=txt[::-1]
#     for char in reverser:
#         print(char)


# txt=input()
# spell(txt)

"""Programation oriented objects"""

"""Class"""
# class Cat:
#     def __init__(self,color,legs):
#         self.color=color
#         self.legs=legs
#         print("hi your color is",color," and your legs is ",legs)

# phoenix = Cat('orange',4)
# tommy = Cat('black',3)

# print(phoenix.color)

# class Dog:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

#     def saludar(self):
#         print("woof")
    
#     def data(self):
#         print("wooff woof my name is: ",self.name," and my color is: ",self.color)

# Max=Dog("max","brown")
# Max.saludar()
# Max.data()

# class Animal:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

# class Dog(Animal):
#     def bark(self):
#         print("woof")

# class Cat(Animal):
#     def miau(self):
#         print("miau")

# cat1=Cat("toon","green")
# dog1=Dog("toon","green")

# cat1.miau()
# dog1.bark()

# class Wolf:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def bark(self):
#         print("grrrr")

# class Dog(Wolf):
#     def bark(self):
#         print("wooof")

# mac=Dog("max","brown")
# mac.bark()


# from turtle import width


# class A:
#     def spam(self):
#         print(1)

# class B(A):
#     def spam(self):
#         print(2)
#         super().spam()

# B().spam(

# )

"""Exercise perimeter the rectangle"""


# class Shape:
#     def __init__(self,width,heigth):
#         self.width=width
#         self.heigth=heigth
    
#     def area(self):
#         resultArea=self.width*self.heigth
#         print(str(resultArea))

# class Rectangle(Shape):
#     def perimeter(self):
#         resultPerimeter=2*(self.width+self.heigth)
#         print(str(resultPerimeter))


# width=int(input("Width: "))
# heigth=int(input("Height: "))

# firstRectangle=Rectangle(width,heigth)

# firstRectangle.area()
# firstRectangle.perimeter()


"""Method magics are the method will be called in the start with __"""


# class Vector2d:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __add__(self,other):
#         return Vector2d(self.x+other.x,self.y+other.y)

# first=Vector2d(5,7)
# second=Vector2d(3,9)

# result=first+second

# print (result.x)
# print (result.y)


"""
More methos magics
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
"""

# class SpecialString:
#     def __init__(self,cont):
#         self.cont = cont

#     def __truediv__(self,other):
#         line ="="*len(other.cont)
#         return "\n".join([self.cont,line,other.cont])

# spam= SpecialString("spam")
# hello= SpecialString("hello World")

# print(spam/hello)

"""
More method magics for comparisions
__it__ for <
__ie__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

"""
# class SpecialString:
#     def __init__(self,cont):
#         self.cont = cont
#     def __gt__(self,other):
#         for index in range(len(other.cont+1)):
#             result= other.cont[:index]+">"+self.cont
#             result+= ">"+other.cont[index:]
#             print(result)

# spam= SpecialString("spam")
# hello= SpecialString("hello")
# spam>hello

"""
Other more method magics
__len__ for len
__getitem__ for get indexar
__setitem__ for set asignar
__delitem__ for delete
__iter__ for iter
__contains__ for in
__call__ for call objects in functions
__str__ for string
__int__ for integer 
"""

# import random
# 
# 
# class Vaguelist:
    # def __init__(self,cont):
        # self.cont = cont
    # def __getitem__(self,index):
        # return self.cont[index+random.randint(-1,1)]
    # def __len__(self):
        # return random.randint(0,len(self.cont)*2)
# 
# vague_list = Vaguelist(["A","B","C","D","E","F","G","H","I"])
# 
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])



"""Ocultacion de  datos"""
# class Queue:
#     def __init__(self,contents):
#         self._hiddenList = list(contents)#the under core say this attribute is private and 2 is more private
    
#     def push(self,value):
#         return self._hiddenList.insert(0,value)
#     def pop(self):
#         return self._hiddenList.pop(-1)

#     def __repr__(self):
#         return "Queue({})".format(self._hiddenList)

# queue=Queue([1,2,3,4])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue._hiddenList)

# class Spam:
#     __egg=888
#     def printEgg(self):
#         print(self.__egg)

# s=Spam()
# s.printEgg()
# print(s._Spam__egg)

"""Is Palindrome"""

# text=input("Please enter the word or text for comprobate is palindrome: ")

# def validationPalindrome(text):
#     if text == text[::-1]:
#         return True
#     else:
#         return False



# print(validationPalindrome(text))

"""Method of class"""
# class Rectangle:
#     def __init__(self,width,heigth):
#         self.width = width
#         self.heigth = heigth
    
#     def calculate_area(self):
#         return self.width * self.heigth

#     @classmethod
#     def new_square(cls,side_length):
#         return cls(side_length,side_length)

# square= Rectangle.new_square(5)
# print(square.calculate_area())

"""los metodos estaticos son iguales que los de la clase solo que estos no reciben argumenttos adicionales"""

# class Pizza:
#     def __init__(self,topping):
#         self.topping = topping
#     @staticmethod
#     def validateToppings(topping):
#         if topping=="pineapple":
#             raise ValueError("no pineapples!")
#         else:
#             return True

# ingredients = ["cheese","onions","spam"]
# if all(Pizza.validateToppings(i) for i in ingredients):
#     pizza= Pizza(ingredients)

"""
propertys
"""
# class Pizza:
#     def __init__(self,toppings):
#         self.toppings = toppings

#     @property
#     def pineapple_allowed(self):
#         result=False
#         return result


# pizza = Pizza(['cheese','onions','spam'])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed=True

# class Employee:
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#     @property
#     def fullName(self):
#         return "{} {}".format(self.first, self.last)
    
#     @property
#     def email(self):
#         return "{}{}@gmail.com".format(self.first, self.last)

# employee1=Employee("John","Gualteros")
# print(employee1.first)
# print(employee1.last)
# print(employee1.email)
# print(employee1.fullName)

# class Pizza:
#     def __init__(self,toppings):
#         self.toppings = toppings
#         self.pineapple_allowed=False
    
#     @property
#     def pineapple_allowed(self):
#         return self.pineapple_allowed

#     @pineapple_allowed.setter

#     def pineapple_allowed(self,value):
#         if value:
#             password = input("Enter password: ")
#         if password=="SwOrdf1sh":
#             self.pineapple_allowed = value
#         else:
#             raise ValueError("Invalid password")

# pizza=Pizza(["cheese", "orange"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed=True
# print(pizza.pineapple_allowed)
"""Module 2 for python for intermediate"""
"""Game of shots"""

class Enemy:
    name=""
    lives=0
    def __init__(self,name,lives):
        self.name = name
        self.lives = lives
    def hit(self):
        self.lives-=1
        if self.lives<=0:
            print(self.name+' killed')
        else:
            print(self.name+' has ' + str(self.lives) +' lives' )

class Monster(Enemy):
    def __init__(self):
        super().__init__('Monster',3)


class Alien(Enemy):
    def __init__(self):
        super().__init__('Alien',5)


m=Monster()
a=Alien()

while True:
    x=input().lower()
    if x=='gun':
        m.hit()

    if x=='laser':
        a.hit()
    if x== 'exit':
        break


