def add_2():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    print "The sum of the given two numbers is", a+b

def add_3():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    c = input("Enter the third number: ")
    print "The sum of the given three numbers is", a+b+c

def add_4():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    c = input("Enter the third number: ")
    d = input("Enter the fourth number: ")
    print "The sum of the given four numbers is", a+b+c+d

print "MENU"
print "1) Add two numbers"
print "2) Add three numbers"
print "3) Add four numbers"
print "4) EXIT"
ch = input("Enter your choice: ")
if(ch == 1):
    add_2()
elif(ch == 2):
    add_3()
elif(ch == 3):
    add_4()
else:
    print "EXITING......"
    exit()

