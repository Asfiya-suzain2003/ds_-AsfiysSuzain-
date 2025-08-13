import pandas as pd

# Create dataframe
data = {
    "Sentiment": ["Fear", "Neutral", "Greed"],
    "Average_PnL": [-5000, 2000, 7000],
    "Total_Volume_USD": [1000000, 1500000, 2000000],
    "Buy_Count": [450, 600, 750],
    "Sell_Count": [550, 600, 450]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv('summary_by_sentiment.csv', index=False)

# Load it back
df = pd.read_csv('summary_by_sentiment.csv')
print(df)
