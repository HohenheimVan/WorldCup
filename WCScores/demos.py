
import locale


# d = datetime.datetime.now()
# print(d.strftime("%A"))
# locale.setlocale(locale.LC_TIME, 'pl_PL.utf8')
# print(d.strftime("%A"))

from datetime import datetime, timedelta

s1 = '10.06.2018 17:54:55'
s2 = '10.06.2018 18:54:55'
FMT = '%d.%m.%Y %H:%M:%S'

tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)


if tdelta.seconds <= 0 or tdelta.days < 0:
    print('nie mozna')
print(tdelta)