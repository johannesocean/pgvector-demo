from pathlib import Path
from configparser import ConfigParser

from app import DB_INIT_FILE


def db_config(filename: Path = DB_INIT_FILE, section: str = 'postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        db = {param[0]: param[1] for param in params}
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return db
