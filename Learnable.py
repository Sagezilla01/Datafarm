import csv
import datetime
import numpy as np
import pandas


def nth_most_rate(arr,n):
    d = dict((x,arr.count(x)) for x in set(arr))
    value = sorted(d.values(), reverse = True)
    nthrepeat = value[n-1]

    for (key,val) in d.items():
        if val == nthrepeat:
            return key



a = [1,2,3,4,5,6,7,92,3,2,35,9,2,43,4,9,9,9]




print(nth_most_rate(a,2))
