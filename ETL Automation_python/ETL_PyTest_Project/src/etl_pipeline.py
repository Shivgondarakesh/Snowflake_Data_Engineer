from pathlib import Path
from extract import read_customers,read_orders
from transform import transform_data
from load import save_output
base=Path(__file__).resolve().parent.parent
customers=read_customers(base/"data/customers.csv")
orders=read_orders(base/"data/orders.csv")
result=transform_data(customers,orders)
save_output(result,base/"output/orders_transformed.csv")
print("ETL Completed")


#%%
# Define the string
original_string = "Malayalam"

# 1. Reverse the string
def is_palindrome(original_string):
    return original_string == original_string[::-1]

print(is_palindrome("Malayalam"))