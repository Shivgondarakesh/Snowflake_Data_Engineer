from pathlib import Path
from extract import read_customers,read_orders
from transform import transform_data
from load import save_output
from logger import logger

def run_etl():
 base=Path(__file__).resolve().parent.parent
 try:
  c=read_customers(base/"data/customers.csv")
  o=read_orders(base/"data/orders.csv")
  r=transform_data(c,o)
  save_output(r,base/"output/orders_transformed.csv")
  logger.info("ETL completed")
 except Exception as e:
  logger.exception(f"ETL failed: {e}")
  raise

if __name__=="__main__":
 run_etl()
