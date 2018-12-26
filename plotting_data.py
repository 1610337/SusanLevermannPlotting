import pandas as ps
import numpy as np
import json

f = open("msci.txt", "r")
f = f.read()
print(str(f))
#print(f)
y = json.loads(str(f))
print(type(y))

'''
y[0] -- 'caption': 'Worldwide - Original', 'benchmark_name': 'MSCI World',
y[1] -- 'caption': 'Worldwide - with positive price momentum', 'benchmark_name': 'MSCI World',
returns a dic
keys:
dict_keys(['id', 'caption', 'benchmark_name', 'historicalData', 'historicalDataRelative', 'historicalCountData'])
'''

# This is what i need
print(y[0]["historicalData"][1])

for val in y[0]["historicalData"]:
    print(val)
