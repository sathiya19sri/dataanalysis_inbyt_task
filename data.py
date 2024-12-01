# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = r"C:\Users\sathi\OneDrive\Documents\AMAZONsales report.csv"  # Update the path to your file
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}.")
    exit()

# Display dataset overview
print("Dataset Overview:")
print(data.head())
print("\nDataset Info:")
print(data.info())
print("\nMissing Values:")
print(data.isnull().sum())

# 1. Sales Overview
try:
    print("\n--- Sales Overview ---")
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  
    data.dropna(subset=['Date'], inplace=True)  
    data['Year-Month'] = data['Order Date'].dt.to_period('M')
    sales_trend = data.groupby('Year-Month')['Amount'].sum()

    plt.figure(figsize=(12, 6))
    sales_trend.plot(kind='line', marker='o', title='Sales Trend Over Time', ylabel='Total Sales', xlabel='Year-Month')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
except KeyError as e:
    print(f"Error: Missing column - {e}")

# 2. Product Analysis
try:
    print("\n--- Product Analysis ---")
    category_sales = data.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    print("\nTop Categories by Sales:")
    print(category_sales)

    plt.figure(figsize=(10, 6))
    category_sales.plot(kind='bar', title='Top Categories by Sales', ylabel='Sales Amount', xlabel='Category')
    plt.xticks(rotation=45)
    plt.show()

    size_distribution = data['Size'].value_counts()
    print("\nSize Distribution:")
    print(size_distribution)

    plt.figure(figsize=(10, 6))
    size_distribution.plot(kind='bar', title='Size Distribution', ylabel='Count', xlabel='Size')
    plt.xticks(rotation=45)
    plt.show()
except KeyError as e:
    print(f"Error: Missing column - {e}")

# 3. Fulfillment Analysis
try:
    print("\n--- Fulfillment Analysis ---")
    fulfillment_method = data['Fulfillment'].value_counts()
    print("\nFulfillment Distribution:")
    print(fulfillment_method)

    plt.figure(figsize=(8, 5))
    fulfillment_method.plot(kind='pie', autopct='%1.1f%%', title='Fulfillment')
    plt.ylabel('')
    plt.show()
except KeyError as e:
    print(f"Error: Missing column - {e}")

# 4. Customer Segmentation
try:
    print("\n--- Customer Segmentation ---")
    location_sales = data.groupby('Ship-city')['Amount'].sum().sort_values(ascending=False)
    print("\nTop Locations by Sales:")
    print(location_sales.head(10))

    plt.figure(figsize=(10, 6))
    location_sales.head(10).plot(kind='bar', title='Top 10 Locations by Sales', ylabel='Amount', xlabel='City')
    plt.xticks(rotation=45)
    plt.show()

    # Segmentation based on buying behavior (e.g., frequency)
    customer_behavior = data['Customer ID'].value_counts()
    print("\nTop Customers by Purchase Frequency:")
    print(customer_behavior.head(10))

    plt.figure(figsize=(10, 6))
    customer_behavior.head(10).plot(kind='bar', title='Top Customers by Purchase Frequency', ylabel='Order Count', xlabel='Customer ID')
    plt.xticks(rotation=45)
    plt.show()
except KeyError as e:
    print(f"Error: Missing column - {e}")

# Save processed data for further analysis
processed_data_path = r"C\Users\sathi\OneDrive\Documents\Processed_AMAZONsales report.csv"  # Update the path to save file
try:
    data.to_csv(processed_data_path, index=False)
    print(f"\nProcessed data saved to {processed_data_path}")
except Exception as e:
    print(f"Error saving processed data: {e}")
