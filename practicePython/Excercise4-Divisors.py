"""
Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

    

def findDivisors(x):
    y=[]
    for i in range(2,x):
        b = int(x) % i
        #print(str(x) + " % " + str(i) + " is " + str(b) )
        if b==0:
            y.append(i)
        
    y=list(dict.fromkeys(y))
    y.sort()
    print("Numbers that divide evenly into " + str(x) + "...")
    print(y)
    
def isNumber(s) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    print("Enter a number...")
    userNumber=input()

    while not isNumber(userNumber):
        print("Enter a number...")
        userNumber=input()
        
    findDivisors(int(userNumber))

main()
    