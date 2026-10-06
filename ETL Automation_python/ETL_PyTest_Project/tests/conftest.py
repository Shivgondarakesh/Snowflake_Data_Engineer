import pytest
import pandas as pd

@pytest.fixture
def customer_data():
 return pd.DataFrame({"customer_id":[1,2,3,4],"customer_name":["John","Mary","David","Sara"],"city":["Bangalore","Mumbai","Delhi","Chennai"]})

@pytest.fixture
def order_data():
 return pd.DataFrame({"order_id":[101,102,103,104],"customer_id":[1,2,3,4],"amount":[2500,4500,1800,3200]})

@pytest.fixture
def transformed_data(customer_data,order_data):
 m=order_data.merge(customer_data,on="customer_id")
 m["amount_category"]=m["amount"].apply(lambda x:"High" if x>=3000 else "Low")
 return m
