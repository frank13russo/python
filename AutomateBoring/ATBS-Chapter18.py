import pyautogui
import time
import logging
import os


currentWorkingDirectory=os.getcwd()
currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__)) # /a/b/c/d/e
os.chdir(currentWorkingDirectory)
logging.basicConfig(filename='ch18log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start')
logging.debug('Current working directory = '+str(currentWorkingDirectory))
logging.debug('Current Screen Resolution = ' +str(pyautogui.size()))

print('Press Ctrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        #pyautogui.moveTo()
        pyautogui.moveRel
        time.sleep(1)
        pyautogui.PAUSE=1
except KeyboardInterrupt:
    print('\nDone.')
    
print(positionStr, end='')
print('\b' * len(positionStr), end='', flush=True)

        