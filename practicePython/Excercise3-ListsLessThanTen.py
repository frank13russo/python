#Read in a csv file that contains numbers
#Verify that it contains only ints or floats
#Store data in a list
#loop over list and create a new list from this list of all of the numbers in it less than X
def generateRandomcsv():
    #import pandas
    import random
    import csv
    minSize=10
    maxSize=9999
    size=random.randint(minSize,maxSize)
    myList=[]
    outputFile = open('randomcsv.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    for i in range(size):
        myNumber=str(random.randint(0,maxSize))
        outputWriter.writerow([myNumber])
        #outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
        #outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
        #outputWriter.writerow([1, 2, 3.141592, 4])
    outputFile.close()
    
def pickFileFromWindows():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()
    

def getSmallNumbers(list,x):
    #list = [4,3,1,5,"xyz",9,10,11]
    #x=5
    list2 = []
    for i in range(len(list)):
        element = str(list[i])
        #print(type(element))
        #print(element)
        if int(element) < x:
            list2.append(element)
            #print (i)
    list2.sort()
    
    for j in range(len(list2):
        print(list2[j])
    
def makelistfromCSV(exampleFile):
    import csv
    with open(exampleFile) as f:
        reader=csv.reader(f)
        my_list=list(reader)
    return my_list

def makeList(fileName):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    import pandas as pd 
    df = pd.read_csv(fileName, sep=',', header=None,squeeze=True)
    #print(type(df))
    numRows=int(len(df))
    #numColumns=len(df.columns)
    toList=df.values.tolist()
    return toList
    
    
def main():
    generateRandomcsv()
    filePath=pickFileFromWindows()
    csvList=makeList(filePath)
    #csvList=makelistfromCSV(filePath)    
    getSmallNumbers(csvList,20)
    
main()

    
    