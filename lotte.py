import pandas_datareader as wb
import pandas as pd
import datetime
import matplotlib.pyplot as plt

pd.set_option('precision', 3)

start = datetime.datetime(2016, 8, 2)
end = datetime.datetime(2017, 11, 7)
df_null = wb.DataReader("004990.KS","yahoo",start,end)
df = df_null.dropna()

kospi_chart = df.Close.plot(style='b')
kospi_chart.set_title("Lotte Confectionery")
kospi_chart.set_ylabel("Price")
kospi_chart.set_xlim(str(start), str(end))

print(df)
print("Close Median", df['Close'].median())
print()
print(df['Close'].describe())
print()
print(df.corr())
print()

original_price = df.iloc[0,3]
nextday_price = df.iloc[1,3]
current_price = df.iloc[-1,3]
month_after_price = df.iloc[30,3]

nextday_change = ((nextday_price-original_price) / original_price)
month_change = ((month_after_price-original_price) / original_price)
current_change = ((current_price-original_price) / original_price)

print("Next day Change: {:.2%}.".format(nextday_change))
print("Month After Change: {:.2%}.".format(month_change))
print("Current Change: {:.2%}.".format(current_change))

plt.show()