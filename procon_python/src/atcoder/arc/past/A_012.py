day=input()
weekday=['Monday','Tuesday','Wednesday','Thursday','Friday']
if(day in weekday):
    print(5-weekday.index(day))
else:
    print(0)