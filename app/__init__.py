from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parents[1]
DB_INIT_FILE = BASE_DIR / 'database.ini'
