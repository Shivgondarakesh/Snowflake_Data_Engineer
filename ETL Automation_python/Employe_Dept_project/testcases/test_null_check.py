from utilities.csv_reader import read_csv
def test_null_values():
 assert read_csv("data/employee_target.csv").isnull().sum().sum()==0
