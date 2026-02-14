
import pandas as pd

df = pd.read_csv("saas_customer_churn_synthetic.csv")

print("Total Customers:", len(df))
print("Churn Rate:", df['churn'].mean()*100)

print("\nChurn by Plan")
print(df.groupby('plan')['churn'].mean())

print("\nAverage Tenure")
print(df['tenure_months'].mean())
