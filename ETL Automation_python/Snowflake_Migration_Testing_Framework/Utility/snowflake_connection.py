import yaml
import snowflake.connector
from pathlib import Path

def get_connection():
    cfg=yaml.safe_load(open(Path(__file__).parents[1]/'Config'/'config.yaml'))
    s=cfg['snowflake']
    return snowflake.connector.connect(user=s['user'],password=s['password'],account=s['account'],warehouse=s['warehouse'],database=s['database'],schema=s['schema'])
