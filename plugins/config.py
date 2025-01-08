import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8074828263:AAG3fi-T5l9dZu4Auru995BvgjUP4_vrCrw")
    
    API_ID = int(os.environ.get("API_ID", "21894814"))
    
    API_HASH = os.environ.get("API_HASH", "4366bdf6ed33089c363df8e4d7b9a1b5")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = "BQFOFp4AkTE_40L1OSkae-VwGi66Y2zcLeczr9pvu_pqPK-5PdUyhVlHeopyf6ZkoQlwZwXSA1ZzQb8Q6YXqJBKeEmkdvGFtV2Oa95RIGUZ_BtxlHrA8iVfk6CWBlwbLd3XHYWtWXdJNUJgD5xrCQ0HJ3mlUpACeAMz1L15e5eFEBNeBDeHSiRT2AKUXia7E_YYDHOmgQ0uW9G8nzjkq-HUENsubLVZgjGs7IxZIVsLyR3Nkjj4fcA6VnLv7BDO_jIP24S-ZX-TmLhziNIk7e5NYFF2wffwBAhMESnsH_-1U6RGhXK8xGxb1L0-q3RMuJo1TPfuI4le0YBxTQveAXZfWvoTNQAAAAAHhTBnnAQ"
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb-srv://uploadbotv2:uploadbotv2@cluster0.ttaccxr.mongodb.net/ 7retryWrites=true&w= majority")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "Mila_walkar_bot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-10023676418"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-10023676418")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5071005351"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mila_walkar_bot")
                                  
