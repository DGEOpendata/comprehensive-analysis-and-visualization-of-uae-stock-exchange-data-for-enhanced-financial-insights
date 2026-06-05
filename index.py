python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (assuming it's in CSV format and locally available)
dataset_path = "Daily_Market_Bulletin.csv"
data = pd.read_csv(dataset_path)

# Display the first few rows of the dataset
print(data.head())

# Filter data for specific company (e.g., ADNOC Logistics & Services)
company_data = data[data['Company Name'] == 'ADNOC Logistics & Services']

# Plot the last 52-week high and low prices for the company
plt.figure(figsize=(12, 6))
plt.plot(company_data['Date'], company_data['52-Week High'], label='52-Week High', color='green')
plt.plot(company_data['Date'], company_data['52-Week Low'], label='52-Week Low', color='red')
plt.title('52-Week High & Low Prices for ADNOC Logistics & Services')
plt.xlabel('Date')
plt.ylabel('Price (AED)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate sectoral performance
sector_performance = data.groupby('Sector')['Percentage Change'].mean().sort_values(ascending=False)

# Plot sectoral performance
plt.figure(figsize=(10, 6))
sns.barplot(x=sector_performance.values, y=sector_performance.index, palette='viridis')
plt.title('Average Sectoral Performance')
plt.xlabel('Average Percentage Change')
plt.ylabel('Sector')
plt.show()
