# FinTech Payment Data Analysis (Beginner Project)

## Project overview
Analyze a **fictional sample** of payment transactions to practice data cleaning, SQL, Python, and business reporting. This is a learning project and is not affiliated with Razorpay or based on real company data.

## Questions answered
- How many transactions are in the sample?
- What is the success rate?
- What is the total value of successful payments?
- Which payment methods have the most failures?
- How does successful payment value change by date?
- Which categories contribute the most successful payment value?

## Tools
- Python
- Pandas
- Matplotlib
- SQL (queries included in `sql/analysis.sql`)

## Project structure
```text
fintech_payment_analysis_project/
├── data/transactions.csv
├── sql/analysis.sql
├── analyze.py
├── requirements.txt
└── README.md
```

## Run locally
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python analyze.py`
5. The script prints summary metrics and saves charts in `outputs/`.

## Data dictionary
- `transaction_id`: fictional transaction identifier
- `transaction_date`: transaction date
- `payment_method`: UPI, Card, NetBanking, or Wallet
- `status`: Success or Failed
- `amount_inr`: transaction amount in INR
- `category`: fictional merchant category

## Data quality checks
The sample intentionally includes a missing category and a duplicate transaction ID so you can demonstrate cleaning. The analysis script removes duplicate transaction IDs and fills missing categories with `Unknown`.

## Important
All transaction data is synthetic and fictional. Do not describe this as Razorpay internal data or claim business results are from a real payment company. Explain it as a personal portfolio project using sample data.
