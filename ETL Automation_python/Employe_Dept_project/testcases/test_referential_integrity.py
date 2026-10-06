from utilities.csv_reader import read_csv
def test_department_mapping():
 employee=read_csv("data/employee.csv"); department=read_csv("data/department.csv")
 assert len(employee[~employee["dept_id"].isin(department["dept_id"])])==0
