#Time and Sleep
#Stopwatch
import time

def sleepExample(x,y):
    
    for i in range(x):
        print ('Tick')
        time.sleep(y)
        print('Tock')

#sleepExample(3,1)

def calcProd(numbers):
    
    product=1
    for i in range(1,numbers):
        product=product*i
    return product

starTime=time.time()
prod=calcProd(5000)
endTime=time.time()
deltaTime=round(endTime-starTime,2)
print('Took %s seconds to calculate.' %(deltaTime))

#! python3
# stopwatch py

print('Press ENTER to begin.  Afterwards, press ENTER to "click" the stopwatch.')
print('Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTimelapNum =1

try: while True:
    input()
    lapTime=round(time.time() - lastTime,3)
    totalTime = round(time.time() - startTIme, 3)
    print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
    lapNum += 1
    lastTime = time.time() # reset the last lap time
    except KeyboardInterrupt:
        print('\nDone.')