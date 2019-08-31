import random
"""
and write a program that returns a list 
that contains only the elements that are common between the lists 
"""

def findCommonElements(a,b):
    a.sort()
    b.sort()
    commonElements=[]
    for i in b:
        if i in a and i not in commonElements:
            commonElements.append(i)
            
    return commonElements

def main():
    x=random.randint(1,50)
    y=random.randint(1,50)
    a = [random.randint(0,x) for i in range(x)]
    b = [random.randint(0,y) for i in range(y)]
    
    c= findCommonElements(a,b)
    c.sort()
    print(c)

main()