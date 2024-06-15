import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
y=datetime.datetime(1999,12,24)
print(y)
print(y.strftime("%w"))# to show weak
print(y.strftime("%A")) #to show day
print(y.strftime("%a"))# short form of day(we use a)
print(y.strftime("%B"))#mounth
print(y.strftime("%b"))
