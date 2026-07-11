import pyttsx3



def add2():
     engine=pyttsx3.init()
     engine.say("Enter first number:")
     engine.runAndWait()
     num1=int(input("Enter first number:"))
     engine=pyttsx3.init()
     engine.say("Enter second number:")
     engine.runAndWait()
     num2=int(input('Enter second number:'))
     sum=num1+num2
     engine=pyttsx3.init()
     engine.say("Sum is:")
     engine.runAndWait()
     print("Sum is:",sum)

def add3():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     sum=num1+num2
     print("Sum is:",sum)

def add4():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     sum=num1+num2+num3+num4
     print("Sum is:",sum)     

def add5():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     num5=int(input('Enter fifth number:'))
     sum=num1+num2+num3+num4+num5
     print("Sum is:",sum)     

def sub2():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     sub=num1-num2
     print("Substraction is:",sub)

def sub3():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     sub=num1-num2-num3
     print("Subtaction is:",sub)

def sub4():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     sub=num1-num2-num3-num4
     print("Substraction is:",sub)  

def sub5():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     num5=int(input('Enter fifth number:'))
     sub=num1-num2-num3-num4-num5
     print("Substraction is:",sub) 

def mul2():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     mul=num1*num2
     print("Multiplication is:",mul)

def mul3():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     mul=num1*num2*num3
     print("Multiplication is:",mul)

def mul4():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     mul=num1*num2*num3*num4
     print("Multiplication is:",mul)

def mul5():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     num5=int(input('Enter fifth number:'))
     mul=num1*num2*num3*num4*num5
     print("Multiplication is:",mul)

def div2():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     div=num1*num2
     print("Division is:",div)

def div3():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     div=num1/num2/num3
     print("Division is:",div)

def div4():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     div=(num1/num2)/(num3/num4)
     print("Division is:",div)     

def div5():
     num1=int(input("Enter first number:"))
     num2=int(input('Enter second number:'))
     num3=int(input('Enter third number:'))
     num4=int(input('Enter forth number:'))
     num5=int(input('Enter fifth number:'))
     div=(num1/num2)/(num3/num4)/(num5)
     print("Division is:",div)

     
print(add2())