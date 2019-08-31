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
    x=random.randint(1,20)
    y=random.randint(1,20)
    a = [random.randint(0,x) for i in range(x)]
    b = [random.randint(0,y) for i in range(y)]
    
    c= findCommonElements(a,b)
    c.sort()
    print("Common elements between the two lists of numbers...")
    print(c)

def alternateMain():
    #List of 10 randomly chosen numbers between 1-100, no duplicates in each list
    x=random.sample(range(1,25), 10)
    y=random.sample(range(1,25), 10)
    z=findCommonElements(x,y)
    z.sort()
    print("Common elements between the two lists of numbers...")
    print(z)
    

main()
alternateMain()