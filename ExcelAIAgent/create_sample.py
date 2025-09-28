import pandas as pd

# Create sample sales data
sample_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [12000, 15000, 18000, 16000, 22000, 25000],
    'Expenses': [8000, 9000, 10000, 9500, 12000, 13000],
    'Profit': [4000, 6000, 8000, 6500, 10000, 12000],
    'Customers': [150, 180, 220, 200, 280, 320]
}

# Create DataFrame and save as Excel
df = pd.DataFrame(sample_data)
df.to_excel('sales_data.xlsx', index=False)
print("✅ Sample Excel file created: sales_data.xlsx")
print("\n📊 Sample Data:")
print(df)
