import bisect
from decimal import Decimal, ROUND_HALF_UP
deg,dis=map(int,input().split())
direct=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
speed=[0,3,16,34,55,80,108,139,172,208,245,285,327]
wind_power=bisect.bisect(speed,Decimal(dis/6).quantize(Decimal('0'), rounding=ROUND_HALF_UP))-1
print((direct[(deg*10+1125)//2250] if wind_power != 0 else "C")+" "+str(wind_power))