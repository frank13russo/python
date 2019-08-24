#box print program
#prints a ascii picture of a box of width and hate

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character.')
        
    if width <=2 or height <=2:
        raise Exception('Width and Height must both be > 2')
    widthSpacingChar='-'
    xsymbol=symbol+widthSpacingChar
    ysymbol=symbol
    print(xsymbol*width)
    for i in range(height-2):
        print(symbol + ((' '+widthSpacingChar) *(width - 2)) + xsymbol)
    print(xsymbol*width)

def main():
    for sym, w, h in (('c',10,10),('0',20,5),('x',1,3),('ZZ',3,3)):
        try:
            boxPrint(sym,w,h)
        except Exception as err:
            print('An exception happened: ' + str(err))

#Assertions
#Sanity check to make sure code isn't doing something obviously wrong.
#Example:  Traffic Light Simulation

main()  
 
        
                        
            
    