import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# Create Revenue Column
df['revenue'] = df['units_sold'] * df['price']

# Total Revenue
total_revenue = df['revenue'].sum()
print("\nTotal Revenue:", total_revenue)

# Region-wise Revenue
region_revenue = df.groupby('region')['revenue'].sum()
print("\nRegion-wise Revenue:")
print(region_revenue)

# Product-wise Sales
product_sales = df.groupby('product')['units_sold'].sum()
print("\nProduct-wise Units Sold:")
print(product_sales)

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Plot Revenue by Region
region_revenue.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.savefig("region_revenue.png")
plt.close()
