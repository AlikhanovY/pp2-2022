import datetime 
a=-1
now=datetime.datetime.now()
yes=datetime.datetime.now()-datetime.timedelta(days=1)
tom=datetime.datetime.now()+datetime.timedelta(days=1)
print(now, yes, tom)