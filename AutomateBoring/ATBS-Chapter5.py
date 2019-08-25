#Dictionary

import pprint

#Dictionary example

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('The size of my cat is ' + myCat['size'])

print(10*'-')
    
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

print(10*'-')    

for k in spam.keys():
    print(k)