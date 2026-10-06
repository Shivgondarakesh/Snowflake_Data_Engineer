import pytest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent/"src"))
from extract import read_customers

def test_invalid_file():
 with pytest.raises(Exception):
  read_customers("missing.csv")
