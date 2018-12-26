import pandas as pd
import numpy as np
import json
import datetime
import matplotlib.pyplot as plt


f = open("msci.txt", "r")
f = f.read()
print(str(f))
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
print(y[0]["historicalDataRelative"][1])

portfolio_vals = [val["portfolio_return"] for val in y[0]["historicalData"]]
portfolio_vals_rel = [val["portfolio_return"] for val in y[0]["historicalDataRelative"]]
bench_vals = [val["benchmark_return"] for val in y[0]["historicalData"]]
bench_vals_rel = [val["benchmark_return"] for val in y[0]["historicalDataRelative"]]
date_keys = [datetime.datetime(val["date_year"], val["date_month"], 1) for val in y[0]["historicalData"]]


main_df = pd.DataFrame(
    {'portfolio_vals': portfolio_vals,
     #'portfolio_vals_rel' : portfolio_vals_rel,
     'bench_vals': bench_vals,
    # 'bench_vals_rel': bench_vals_rel,
    }, index=date_keys)

plt.plot(main_df["portfolio_vals"])
plt.plot(main_df["bench_vals"])
plt.ylabel('some numbers')
plt.show()

print(np.var(main_df["portfolio_vals"]))
print(np.var(main_df["bench_vals"]))

