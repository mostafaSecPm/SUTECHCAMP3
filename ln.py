import math
import sys

def loge(n,li,ls):
    if math.fabs(li-ls) <= 0.000001:
       return (li+ls)/2.0
    if (math.exp(li)-n)*(math.exp((li+ls)/2.0)-n) < 0:
       return loge(n,li,(li+ls)/2.0)
    else:
       return loge(n,(li+ls)/2.0,ls)

def ln(n):
    if n == 0 or n < 0:
       return "Math Domain Error"
    if n == 1:
       return 0
    if n > 0 and n < 1:
       return loge(n,0,-n-80)
    else:
       return loge(n,0,n)
