import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = os.path.join("data", "transactions.csv")
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")

print("=== DATA QUALITY BEFORE CLEANING ===")
print("Rows:", len(df))
print("Duplicate transaction IDs:", df["transaction_id"].duplicated().sum())
print("Missing values by column:\n", df.isna().sum())

# Basic cleaning
df = df.drop_duplicates(subset=["transaction_id"], keep="first")
df["category"] = df["category"].fillna("Unknown")
df = df.dropna(subset=["transaction_date", "amount_inr", "status"])
df["status"] = df["status"].str.strip().str.title()

successful = df[df["status"] == "Success"]
total_transactions = len(df)
success_count = len(successful)
success_rate = (success_count / total_transactions * 100) if total_transactions else 0
successful_value = successful["amount_inr"].sum()

print("\n=== SUMMARY ===")
print(f"Transactions after cleaning: {total_transactions}")
print(f"Successful transactions: {success_count}")
print(f"Success rate: {success_rate:.1f}%")
print(f"Successful payment value: ₹{successful_value:,.2f}")

print("\n=== PAYMENT METHOD BREAKDOWN ===")
print(df.groupby(["payment_method", "status"]).size().unstack(fill_value=0))

print("\n=== SUCCESSFUL PAYMENT VALUE BY CATEGORY ===")
print(successful.groupby("category")["amount_inr"].sum().sort_values(ascending=False))

# Chart 1: status count
df["status"].value_counts().plot(kind="bar")
plt.title("Transaction Count by Status")
plt.xlabel("Status")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "transaction_status.png"), dpi=150)
plt.close()

# Chart 2: successful value by date
daily = successful.groupby(successful["transaction_date"].dt.date)["amount_inr"].sum()
daily.plot(kind="line", marker="o")
plt.title("Successful Payment Value by Date")
plt.xlabel("Date")
plt.ylabel("Successful Value (INR)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "daily_successful_value.png"), dpi=150)
plt.close()

# Export cleaned data
df.to_csv(os.path.join(OUTPUT_DIR, "cleaned_transactions.csv"), index=False)
print(f"\nSaved charts and cleaned data in '{OUTPUT_DIR}/'.")
