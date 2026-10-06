from Utility.snowflake_connection import get_connection

def fetch_one(query):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(query)
    v=cur.fetchone()[0]
    cur.close();conn.close()
    return v

def test_record_count():
    assert fetch_one('SELECT COUNT(*) FROM SOURCE_SALES') == fetch_one('SELECT COUNT(*) FROM FACT_SALES')

def test_sales_sum():
    assert fetch_one('SELECT COALESCE(SUM(SALES_AMOUNT),0) FROM SOURCE_SALES') == fetch_one('SELECT COALESCE(SUM(SALES_AMOUNT),0) FROM FACT_SALES')

def test_duplicate_records():
    conn=get_connection();cur=conn.cursor()
    cur.execute("SELECT COUNT(*) FROM (SELECT CUSTOMER_ID,COUNT(*) FROM FACT_SALES GROUP BY CUSTOMER_ID HAVING COUNT(*)>1)")
    assert cur.fetchone()[0] == 0
    cur.close();conn.close()
