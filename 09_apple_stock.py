# pandas_exercises 09 Time Series - Apple Stock
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

# Step 4. Check out the type of the columns
# print(apple.dtypes)

# Step 5. Transform the Date column as a datetime type
apple['Date'] = pd.to_datetime(apple['Date'])
# print(apple.dtypes)

# Step 6. Set the date as the index
apple = apple.set_index('Date')
# print(apple.head())

# Step 7. Is there any duplicate dates?
# print(apple.index.has_duplicates)

# Step 8. Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
apple = apple.sort_index()
# print(apple.head())

# Step 9. Get the last business day of each month
apple_resample = apple.resample('BME').last()
# print(apple_resample)

# Step 10. What is the difference in days between the first day and the oldest
days_diff = (apple.index[-1] - apple.index[0]).days
# print(days_diff)

# Step 11. How many months in the data we have?
# print(len(apple_resample))

# Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
# apple['Adj Close'].plot(figsize=(13.5, 9), title='Adjusted Close Price History')
# plt.xlabel('Date')
# plt.ylabel('Price $')
#
# plt.show()

# BONUS: On which date did Apple’s Adj Close have its biggest one-day percentage drop, and how big was the drop?
apple['pct_change'] = apple['Adj Close'].pct_change() * 100
drop_date = apple['pct_change'].idxmin()
drop_pct = apple['pct_change'].min()
drop_date_iloc = apple.index.get_loc(drop_date)
print(f"Biggest percentage drop date: {drop_date}")
print(f"Biggest percentage drop: {drop_pct.round(2)}%")
print(f"Adjusted close price before drop day: {apple['Adj Close'].iloc[drop_date_iloc-1]}")
print(f"Adjusted close price on drop day: {apple.loc[drop_date, 'Adj Close']}")
