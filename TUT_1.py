def function1():
    print('hello world')
    print('Marvin')    
    print('Dickson')
    print('Tina')
    print('Caleb')
    print('Anson')    
    

def function2():
    a = 5 
    b = 7 
    c = 9
    sum = a + b + c
    print(sum)


def function3():
    a= 5
    print(a*a)

def function4():
    a = 5
    b = 7 
    if a < b:
        print('a is smaller than b')
    else: 
        print('a is larger than b')


def advanced_TowelBuilder():  
    a = input("input:")
    a=int(a)
    i = 0
    while i < a:
        print('xxx')
        if (i == a):
          break
        i += 1


def advanced_AdditionCalculator():
    a=input('Please input a int:')
    a=int(a)
    b=input('Please input another int:')
    b=int(b)
    c=a+b
    print('The final result is',c)
    
    
def advanced_ReversedList(): 
    a=input('The list length is:')
    a=int(a)
    while 0 < a:
        print(a)
        if a == 0:
         break
        a -= 1
    
def advanced_SquarePrinter():     
    x=input('Square Size:')
    x=int(x)
    i=0
    j=0
    while i<x:
        j=0
        print(end="\n")
        if x==i:
         break
        while j<x:
         print('[]',end='')
         j += 1
         if j==x:
            break
        i += 1
    

#The Main function edited by Group leader
print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')   #Ask for an integer

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
else:
    print('There is no function', inp)
