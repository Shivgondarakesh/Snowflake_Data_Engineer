def test_join_successful(transformed_data):
 assert len(transformed_data)==4

def test_amount_category_created(transformed_data):
 assert "amount_category" in transformed_data.columns
