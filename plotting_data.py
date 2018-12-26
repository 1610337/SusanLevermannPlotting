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
bench_vals = [val["benchmark_return"] for val in y[0]["historicalData"]]
date_keys = [datetime.datetime(val["date_year"], val["date_month"], 1) for val in y[0]["historicalData"]]

bench_vals_rel = [val["benchmark_return"] for val in y[0]["historicalDataRelative"]]
portfolio_vals_rel = [val["portfolio_return"] for val in y[0]["historicalDataRelative"]]
rels_key = [datetime.datetime(val["date_year"], val["date_month"], 1) for val in y[0]["historicalDataRelative"]]

# remove all after 2017, 10, 1, 0, 0) ?

main_df = pd.DataFrame(
    {'portfolio_vals': portfolio_vals,
     'bench_vals': bench_vals,
    }, index=date_keys)
# TODO refactor and calc vola
rel_DF = pd.DataFrame(
    {'portfolio_vals_rel' : portfolio_vals_rel,
    'bench_vals_rel': bench_vals_rel,
    }, index=rels_key)

main_df2 = rel_DF.join(main_df, how='left')

print(len(rel_DF))
print(len(main_df))
print(len(main_df2))


plt.plot(main_df["portfolio_vals"])
plt.plot(main_df["bench_vals"])
plt.ylabel('some numbers')
plt.show()

print(np.var(main_df2["portfolio_vals_rel"]))
print(np.var(main_df2["bench_vals_rel"]))

