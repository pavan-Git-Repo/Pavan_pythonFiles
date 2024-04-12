import datetime
mytime = datetime.time(2,25)
print(mytime.hour)
print(mytime)
today = datetime.date.today()
print(today)
print(today.ctime())
from datetime import datetime
mydatetime = datetime(2022,4,15,23,30,21)
#year=2022,month=4,date =15,  hour =23,min=30,sec =21
print(mydatetime)
print(mydatetime.replace(month =3,hour=22))
from datetime import date
date1 =date(2022,3,2)
date2 = date(2021,4,23)
result = date1-date2
print(result)

import math
value = 3.9
print(math.floor(value))
print(math.ceil(value))