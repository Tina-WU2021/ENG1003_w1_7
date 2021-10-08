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
    a=input("please input a number:")
    a=int(a)
    print(a*a)
def function4():
    a = 5
    b = 7 
    if a < b:
     print('a=5 b=7')
     print('a is smaller than b')


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
