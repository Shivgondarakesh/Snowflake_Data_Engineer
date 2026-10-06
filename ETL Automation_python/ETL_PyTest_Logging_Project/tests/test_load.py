import pandas as pd
def test_write(tmp_path,transformed_data):
 f=tmp_path/"out.csv"; transformed_data.to_csv(f,index=False)
 assert len(pd.read_csv(f))==4
