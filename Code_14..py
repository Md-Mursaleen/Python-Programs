#Datetime Module in Python.
import datetime
print(dir(datetime))
print(datetime.date.today())
print(datetime.datetime.now())


from datetime import date
today=date.today()
print(today.year)
print(today.month)
print(today.day)
print(date(2019,4,13))

from datetime import time
a=time()
print(a)
b=time(10,40,30)
print(b)
c=time(10,30,40,500)
print(c)
print(c.hour)
print(c.minute)
print(c.second)
print(c.microsecond)


from datetime import datetime
a=datetime(2019,4,12)
print(a)
b=datetime(2019,4,12,20,30,40,600)
print(b)
print(b.year)
print(b.month)
print(b.day)
print(b.hour)
print(b.minute)
print(b.second)
print(b.microsecond)
#Timestamp is the number of seconds between a particular date and 1,Jan 1970 at UTC
#to convert timestamp into date we can use from timestamp() method
print(date.fromtimestamp(123456))

