def test_customer_loaded(customer_data): assert len(customer_data)==4
def test_customer_unique(customer_data): assert customer_data["customer_id"].is_unique
