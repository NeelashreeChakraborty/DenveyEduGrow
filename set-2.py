import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("/content/SET_2.csv")

# Add dummy year for proper datetime parsing
df['month'] = df['month'] + ' 2024'
df['month'] = pd.to_datetime(df['month'], format='%B %Y')

# Sort months
df.sort_values('month', inplace=True)

# Bar chart
plt.figure(figsize=(12, 6))
plt.bar(df['month'].dt.strftime('%b'), df['news_sold'], color='steelblue')
plt.xlabel("Month")
plt.ylabel("News Sold")
plt.title("News Sold per Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Rest of the tasks...
df['percentage_change'] = df['news_sold'].pct_change() * 100
low_sales = df[df['news_sold'] < 2000]
print("\nMonths with news_sold < 2000:\n", low_sales)

df['quarter'] = df['month'].dt.to_period('Q')
quarterly_sales = df.groupby('quarter')['news_sold'].sum().reset_index()
print("\nTotal news sold by quarter:\n", quarterly_sales)

avg = df['news_sold'].mean()
above_avg = df[df['news_sold'] > avg]
above_avg.to_csv("/content/above_average_news_sold.csv", index=False)
print("\nSaved above-average months to 'above_average_news_sold.csv'")