def add2num(a,b):
    sum=a+b
    print("Sum is:",sum)

def avg2num(a,b):
    avg=(a+b)/2
    print("Average is:",avg)

def sqr_num():
    num1=int(input("Enter a number:"))
    num1**=2
    print("Square is:",num1)

def even_odd():
    num=int(input("Enter a number to check even or odd:"))
    if (num%2==0):
        print(num,"is an even number")
    else:
        print(num,"is an odd number") 

def find_greater_smaller():
    num1=int(input("Enter first number:"))
    num2=int(input('Enter second number:'))
    if(num1>num2):
        print(num1,"is greater",num2,"is smaller")
    else:
        print(num2,"is greater",num1,"is smaller")   



add2num(5,6)
avg2num(5,7)
sqr_num()
even_odd()
find_greater_smaller()