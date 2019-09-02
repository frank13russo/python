# Load modules

from matplotlib import pyplot as plt
import pandas as pd
import logging
import os

       
def basicSetup():
    currentWorkingDirectory=os.getcwd()
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Start')
    logging.debug('Initial working directory = '+str(currentWorkingDirectory))
    currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__)) # /a/b/c/d/e
    os.chdir(currentWorkingDirectory)
    #logging.basicConfig(filename='ch18log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Current working directory = '+str(currentWorkingDirectory))
    logging.disable(logging.DEBUG) 

#for some reason my python looks in the directory above the one this file is in.  
basicSetup()

# Load data - GLOBAL

df = pd.read_csv('page_visits.csv')

# Display data
#print(df.head())


  

def pieChart():
    # Calculate survey results
    survey_results = df.groupby('website_goal')\
  	.first_name.count()
   
   # Make a pie chart
    plt.pie(survey_results.values,
            labels=survey_results.index,
            autopct='%d%%'
        )
    plt.title('Why do citizens visit our website?')
    plt.axis('equal')
    plt.show()

#  Look at number of visits per day
def visitsPerday():
    by_day = df.groupby('visit_date').first_name.count()

    plt.figure(figsize=(16, 4))
    ax = plt.subplot()
    plt.plot(by_day.values,
            marker='o', markersize=8, linewidth=3)
    plt.ylabel("Number of Visits")
    ax.set_xticks(range(len(by_day))[::8])
    ax.set_xticklabels(by_day.index[::8], rotation=45)
    plt.show()

#Histogram of age of visitors
def makeHistogram():
    plt.hist(df.age, range=(10, 65), bins=11, edgecolor='white')
    plt.xlabel('Visitor Age')
    plt.ylabel('Number of Visitors')
    plt.title('Histogram of Visitor Age')
    plt.show()
    
def main():
    makeHistogram()

main()