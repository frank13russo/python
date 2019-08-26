import logging
import os

       
def basicSetup():
    currentWorkingDirectory=os.getcwd()
    currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__)) # /a/b/c/d/e
    os.chdir(currentWorkingDirectory)
        #logging.basicConfig(filename='ch18log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Start')
    logging.debug('Current working directory = '+str(currentWorkingDirectory))
        
