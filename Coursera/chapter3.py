def function1():
    x = 0
    if x < 2 :
        print('Small')
    elif x < 10 :
        print('Medium')
    else :
        print('LARGE')
    print('All done')

def function2():
    x=222.0
    if x < 2 :
        print('Below 2')
    elif x >= 2 :
        print('Two or more')
    else :
        print('Something else')

def function3():
    astr = 'Hello Bob'
    istr = int(astr)
    print('First', istr)
    astr = '123'
    istr = int(astr)
    print('Second', istr)

def f4():
    astr = 'Hello Bob'
    istr = 0
    try:
        istr = int(astr)
    except:
        istr = -1
    return istr

"""
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 

Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.

"""

def computeGrossPay():
    overTime=0
    
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    
    if hrs <= 40:
        basePay=hrs*rate
    if hrs > 40:
        basePay=40*rate
        overTime=hrs-40
        extraPay=1.5*overTime*rate
    grossPay = extraPay+basePay
    print(grossPay)   
        
 
computeGrossPay()      


