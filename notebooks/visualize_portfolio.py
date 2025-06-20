# notebooks/visualize_portfolio.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the optimized portfolio data
df = pd.read_csv("output/optimized_portfolio.csv")

# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(df["Allocation"], labels=df["Coin"], autopct="%1.1f%%", startangle=140, colors=["#FFD700", "#8A2BE2"])
plt.title("🧠 Optimized Crypto Portfolio Allocation")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.tight_layout()
plt.show()
