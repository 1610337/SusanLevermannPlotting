import pandas as pd
import numpy as np
import json
import datetime
import matplotlib.pyplot as plt

'''
Hypothetical performance is not necessarily indicative of future results. No representation is being made that any action will achieve profits or losses similar to those displayed. The result may be overstated as neither transaction costs nor bid/ask spreads nor slippage have been considered. Output equally weighted with maximum 5% allocation per position and rebalanced monthly. Holdings are systematically replaced when the screening criteria are not met anymore. No additional buying or selling rules (technical analysis) have been employed.
Due to lack of the full historical data set, this back-test only considers 11 of the 13 factors and therefore the result will deviate from a back-test using the complete data set. Moreover, only stocks with a score of >=5 were considered.

Diest eine deutlich vereinfachte Darstellung getester Kursdaten!
Die Daten aus msci.txt stammen von
    https://meetinvest.com/stockscreener/susan-levermann

'''

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


plt.plot(main_df["portfolio_vals"], 'C1', label='Portfolio - Performance')
#plt.plot((main_df["bench_vals"]), 'C2', label='MSCI World')
plt.plot((main_df["bench_vals"])*13, 'C3', label='MSCI World x 13')
plt.legend()


plt.ylabel('Prozentuale Entwicklung')
plt.xlabel('Jahre')

plt.show()

print(np.var(main_df2["portfolio_vals_rel"]))
print(np.var(main_df2["bench_vals_rel"]))

print(np.std(main_df2["portfolio_vals_rel"], ddof=1))
print(np.std(main_df2["bench_vals_rel"], ddof=1))
print(np.std(main_df2["bench_vals_rel"]*13, ddof=1))
