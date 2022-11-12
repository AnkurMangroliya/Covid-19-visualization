import matplotlib.pyplot as plt
import matplotlib.dates as mdates

%matplotlib inline
plt.style.use('fivethirtyeight')

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv', parse_dates=['Date'])

w = worldwide_df.plot(figsize=(8,4))
w.set_xlabel('Dates')
w.set_ylabel(' # Cases worldwide')
w.title.set_text('Worldwide Covid Insights')

plt.show()
