import pandas as pd
employee=pd.read_csv("data/employee.csv")
department=pd.read_csv("data/department.csv")
target=employee.merge(department,on="dept_id",how="left")
target=target[["emp_id","emp_name","dept_name","salary"]]
target.to_csv("data/employee_target.csv",index=False)
print("ETL completed")

from collections import Counter

def count_characters(text):
    # Method 1: Using the built-in Counter (Recommended)
    return Counter(text)

# Example usage:
input_str = "hello world"
result = count_characters(input_str)
print(result)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

a=7
b=3
c=12

if a>5:
    if b>5:
        print("I")
    elif c>10:
        print ("I")
        if a+b>c:
            print("love")
        else:
            print("coding")
    else:
        print ("python")
else:
    print("hello")







