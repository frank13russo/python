#doing a basic for loop
for i in range(0,5,1): #do for loops always have the range method?  I think so...
    print(i)

#print ("For Loop over")

i=0    
#while loop
while i<5:
    print(i)
    i+=1

def functionHelloWorld():
    print("Hello World")

#example function call
functionHelloWorld()
functionHelloWorld()

def foo(exampleArg):
    print(exampleArg)

foo("Hi")

numbers = [6,3,1,9,7,4,8,9,5,0]
for n in numbers:
    print (n)



#i can't believe python lets you do this.  pythons loops are actually for each loops
def separateList(myList):
    i=0
    mystring=""
    while i <= len(myList):
        mystring.append(myList[i])
        i+=1
    print(mystring)


spam = ['apples', 'bananas','tofu','cats']
spamLength=len(spam)

spam2=spam.append('dogs')

first=spam[0]
second=spam[1]
third=spam[2]
fourth=spam[3]



separateList(spam)
separateList(spam2)
    
