import logging
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent
LOG_DIR=BASE/"logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE=LOG_DIR/"etl.log"
logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s",handlers=[logging.FileHandler(LOG_FILE),logging.StreamHandler()])
logger=logging.getLogger(__name__)
