import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("/content/ SET_3.csv")

# Preview dataset
print("Dataset Preview:\n", df.head())

# 2. Create a pie chart showing the proportion of total news sold by month
plt.figure(figsize=(8, 8))
plt.pie(df['news_sold'], labels=df['month'], autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Total News Sold by Month")
plt.tight_layout()
plt.show()

# 3. Add a cumulative_sales column
df['cumulative_sales'] = df['news_sold'].cumsum()

# 4. Add a column with corresponding month numbers
month_to_num = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df['month_number'] = df['month'].map(month_to_num)

# 5. Display the three months with the lowest news_sold
lowest_months = df.nsmallest(3, 'news_sold')
print("\nThree Months with Lowest News Sold:\n", lowest_months)

# 6. Calculate and interpret standard deviation
std_dev = df['news_sold'].std()
print(f"\nStandard Deviation of news_sold: {std_dev:.2f}")

# Interpretation
mean_sales = df['news_sold'].mean()
print(f"Mean News Sold: {mean_sales:.2f}")
print("\nInterpretation:")
print("The standard deviation shows how much the news sales deviate from the average.")
print(f"A standard deviation of {std_dev:.2f} means that most months have news sales within ±{std_dev:.2f} of the mean ({mean_sales:.2f}).")