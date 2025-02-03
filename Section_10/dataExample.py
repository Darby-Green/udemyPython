from datetime import *
import locale

locale.setlocale(locale.LC_ALL, '')

start = date(2022,2,4)
print(start)

prettyStart = start.strftime('%A %d %B, %Y')
print(prettyStart)

duration = timedelta(days=15)
end = start + duration
print(end)

d1 = timedelta(hours=2)
d2 = timedelta(minutes=120)
d3 = timedelta(seconds=7200)
print(d1, d2, d3, sep=', ')
print(repr(d1), repr(d2), repr(d3), sep=', ')