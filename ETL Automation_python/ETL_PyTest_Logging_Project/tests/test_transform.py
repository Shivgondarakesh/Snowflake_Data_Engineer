def test_category_column(transformed_data): assert "amount_category" in transformed_data.columns
def test_join_count(transformed_data): assert len(transformed_data)==4
