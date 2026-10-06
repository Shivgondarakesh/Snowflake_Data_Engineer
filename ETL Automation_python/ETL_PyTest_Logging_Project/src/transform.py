import pandas as pd
from logger import logger

def transform_data(customers,orders):
 logger.info("Transform started")
 m=pd.merge(orders,customers,on="customer_id",how="left")
 m["amount_category"]=m["amount"].apply(lambda x:"High" if x>=3000 else "Low")
 return m
