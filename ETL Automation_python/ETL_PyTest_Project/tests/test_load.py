import pandas as pd

def test_output_write(tmp_path,transformed_data):
 f=tmp_path/"out.csv"
 transformed_data.to_csv(f,index=False)
 assert f.exists()
 assert len(pd.read_csv(f))==len(transformed_data)
