import datetime

name = input("Give me your name: ")
print("Your name is " + name)

while True:
    try:
        age = int(input("How old are you?"))
    except ValueError:
        print("That is not a valid age")
        continue 
    else:
        break



yearsUntill=100-age
today=datetime.date.today()
thisYear=today.year
print("It is currently the year" + str(thisYear))
year100=thisYear+yearsUntill

print("You will be 100 years old in the year:" + str(year100))
