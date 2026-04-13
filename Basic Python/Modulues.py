import math as m

print(m.pi)
print(m.sqrt(20))
print(m.floor(3.2))
print(m.ceil(3.2))
print(m.factorial(7))

from math import  sqrt, pi, floor, factorial

print(sqrt(20))
print(floor(3.2))
print(factorial(7))

from math import *

print(cos(90))
print(sin(0))


print('___________________________________Random___________________________________')

import random

print(random.randint(1,10), 'This is random')

print(random.random(), 'random float between 0.0 to 1.0')

color = ['REd', 'blue', 'green']
print(random.choice(color), 'random color print')

num = [1,4,2,4,2,3,5,3,2,3,2,3]
print(random.shuffle(num), 'print shuffle function')
print(random.sample(num, 3), 'print sample function')



print('______________________________________Date Time Import___________________________________')

from datetime import datetime, date, timedelta
now = datetime.now()

print('print current time', now)
print(now.year)
print(now.month)
print(now.day)
#print(now.strfime('%B %D, %Y'))
