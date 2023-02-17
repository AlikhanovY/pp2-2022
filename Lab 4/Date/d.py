import datetime 
now=datetime.datetime.now()
then=datetime.datetime(1999,9,9)
sec=now-then
print(f"Total second difference {sec.total_seconds()}")