from utilities.csv_reader import read_csv
def test_duplicate_emp():
 assert read_csv("data/employee_target.csv")["emp_id"].duplicated().sum()==0
