from pathlib import Path
from dotenv import load_dotenv
from utils.env_util import get_env_value

root_path = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=root_path / '.env')

class Config:
    # Geral
    PREFIX: str = "/math-api"
    
    # APP
    APP_VERSION: str = "main"
   
    # Loggers
    LOGGER_LEVEL: str = get_env_value("LOGGER_LEVEL")