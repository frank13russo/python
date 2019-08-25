#box print program
#prints a ascii picture of a box of width and hate
import logging
import os

currentWorkingDirectory=os.getcwd()
currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__)) # /a/b/c/d/e
os.chdir(currentWorkingDirectory)

#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start')

##Try Except Example
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character.')
        
    if width <=2 or height <=2:
        raise Exception('Width and Height must both be > 2')
    widthSpacingChar='='
    midSpacingChar=' '
    xsymbol=symbol+widthSpacingChar
    ysymbol=symbol
    topBotLength=len(xsymbol*width)
    leftRightLength=len(ysymbol*height)
    logging.debug(topBotLength)
    logging.debug(leftRightLength)
    topBot=2*midSpacingChar+(xsymbol*(width-1))+symbol
    print(topBot)
    for i in range(height-2):
        mid=symbol+midSpacingChar + ((widthSpacingChar+midSpacingChar) *(width)) + symbol
        print(mid)
    print(topBot)

def main():
    for sym, w, h in (('c',10,10),('0',20,5),('x',1,3),('ZZ',3,3)):
        try:
            boxPrint(sym,w,h)
        except Exception as err:
            print('An exception happened: ' + str(err))

#Assertions
#Sanity check to make sure code isn't doing something obviously wrong.
#Example:  Traffic Light Simulation

##Logging example

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total=1
    for i in range(1,n+1): #range is (start, stop, step)
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')


    
#main()  
 
        
                        
            
    