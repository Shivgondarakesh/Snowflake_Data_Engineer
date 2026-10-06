import utilities.csv_reader
def test_row_count():
 assert len(utilities.csv_reader.read_csv("data/employee.csv")) == len(utilities.csv_reader.read_csv("data/employee_target.csv"))
