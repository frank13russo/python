import os
import pandas as pd
import numpy as numpy
import matplotlib
#matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

plt.style.use('ggplot')

fileName='credit_card.csv'

currentWorkingDirectory=os.getcwd()
currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__)) # /a/b/c/d/e
os.chdir(currentWorkingDirectory)

df= pd.DataFrame
numpy.set_printoptions(precision=2)

#need to figure out how to make this so the entire code isn't indented.
if os.path.exists(fileName):
    df = pd.read_csv(fileName) #pd.read_csv reads into a DataFrame
    #print("Rows, Columns")
    #print (df.shape) #.shape returns a tuple representing the dimensionality of the DataFrame
    numRows=int(len(df))
    xList=df["Debit"].tolist()

    rangeExample=range(numRows) #good to look at this in debug to see how range() works
    y=[]
    for i in range(numRows):
        y.append(i)
        
    headings=(df.columns)#pandas array

    debitArray=df["Debit"]
    averageDebit=df["Debit"].mean()
    averageDebitout='{:.2f}'.format(averageDebit) 
    maxDebit=df["Debit"].max() #pandas
    maxDebitout='{:.2f}'.format(maxDebit)
    minDebit=df["Debit"].min() #pandas
    minDebitout='{:.2f}'.format(minDebit)

    output=open('creditCardStats.txt','w+')

    for i in range(len(headings)):
        output.write(" | ") #uses import os
        output.write(headings[i])
        output.write(" | ")

    output.write("\n")
    output.write(" Average Debit = $")
    output.write(averageDebitout)
    output.write("\n")
    output.write("Max Debit = $")
    output.write(maxDebitout)
    output.write("\n")
    output.write("Min Debit = $")
    output.write(minDebitout)
    output.close()
    
    #Plot
    plt.plot(y,xList)
    #plt.plot([1,2,3,4])
    plt.ylabel('$')
    plt.xlabel('Transaction #')
    plt.savefig('CreditCard.png')
    plt.show

else:
    print("File Not Found")

