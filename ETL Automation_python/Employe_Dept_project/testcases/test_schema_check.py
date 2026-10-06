import utilities.csv_reader
def test_schema():
 assert list(utilities.csv_reader.read_csv("data/employee_target.csv").columns) == ["emp_id", "emp_name", "dept_name", "salary"]
