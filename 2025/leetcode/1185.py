class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        yobi=["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if month==1:
            month=13
            year-=1
        elif month==2:
            month=14
            year-=1
        c=int(year/100)
        y=year%100
        gamma=(-2)*c + int(c/4)
        h=(day+int(26*(month+1)/10)+y+int(y/4)+gamma)%7
        return yobi[h]