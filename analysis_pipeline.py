import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

os.makedirs("output", exist_ok=True)

# revenue by product
revenue_product = df.groupby("Product")["Revenue"].sum()

plt.figure()
revenue_product.plot(kind="bar")
plt.title("Revenue by product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("output/revenue_by_product.png")

# revenue by region
revenue_region = df.groupby("Region")["Revenue"].sum()

plt.figure()
revenue_region.plot(kind="bar")
plt.title("Revenue by region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("output/revenue_by_region.png")

# quantity distribution
plt.figure()
df["Quantity"].hist()
plt.title("Distribution of Quantity Sold")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/quantity_distribution.png")

# price vs quantity
plt.figure()
plt.scatter(df["Price"], df["Quantity"])
plt.title("Price vs Quantity Sold")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig("output/price_vs_quantity.png")

# generate summary report
report = f"""
Dataset size: {len(df)}

Total revenue: {df["Revenue"].sum():.2f}

Average price: {df["Price"].mean():.2f}

Best selling product: {revenue_product.idxmax()}
"""

with open("output/summary_report.txt", "w") as f:
    f.write(report)

print("Analysis complete. Report generated.")
