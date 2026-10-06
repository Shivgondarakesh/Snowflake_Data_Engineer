def test_customer_data_loaded(customer_data):
 assert len(customer_data)>0

def test_customer_id_unique(customer_data):
 assert customer_data["customer_id"].is_unique
