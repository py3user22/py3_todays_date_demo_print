#!/bin/python3


from datetime import *
from dateutil.relativedelta import *

print('Display todays date ')
print(date.today())

now = datetime.now()
print(now)

now1 = now + relativedelta(months=1, weeks=1, hour=10)
print(now1)





print('\n-----------------\n')

# --------------------

print('Build a unit converter')
parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

print('\n-----------------\n')

# --------------------

