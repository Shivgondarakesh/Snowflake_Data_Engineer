from utilities.csv_reader import read_csv
def test_salary_sum():
 assert read_csv("data/employee.csv")["salary"].sum()==read_csv("data/employee_target.csv")["salary"].sum()
