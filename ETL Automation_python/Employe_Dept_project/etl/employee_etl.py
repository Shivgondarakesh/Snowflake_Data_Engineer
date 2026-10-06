import pandas as pd
employee=pd.read_csv("data/employee.csv")
department=pd.read_csv("data/department.csv")
target=employee.merge(department,on="dept_id",how="left")
target=target[["emp_id","emp_name","dept_name","salary"]]
target.to_csv("data/employee_target.csv",index=False)
print("ETL completed")