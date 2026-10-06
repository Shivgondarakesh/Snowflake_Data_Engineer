import pandas as pd

def transform_data(customers, orders):
    merged=pd.merge(orders,customers,on="customer_id",how="left")
    merged["amount_category"]=merged["amount"].apply(lambda x:"High" if x>=3000 else "Low")
    return merged
