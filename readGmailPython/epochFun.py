import datetime
from datetime import timedelta,date
import time

print(time.time())
print(datetime.datetime.now())
startDate=datetime.datetime(2000,1,1)
print(startDate)
prettyStartDate=time.strftime("%Y / %m / %d ") #default t=today
print(prettyStartDate)

#prettyEpoch=time.strftime("%Y / %m / %d ",time.time())



def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n) #adds number of days to the start date, returns new date.

start_date = date(2019, 1, 1)
end_date = date(2020, 1, 1)
for single_date in daterange(start_date, end_date):
    print (single_date.strftime("%Y-%m-%d"))

test=(1+1+ \
    1)
print(test)