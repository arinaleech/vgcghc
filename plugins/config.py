import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7619169027:AAG33n3Em3vicp48ADx1_uE80bNZLcbZgSA")
    
    API_ID = int(os.environ.get("API_ID", "21894814"))
    
    API_HASH = os.environ.get("API_HASH", "4366bdf6ed33089c363df8e4d7b9a1b5")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = "BQFOFp4AZtjWNp7An3LRsDWNudDpjrsJbjCDbD8iuyV5cduNEnUGALXlLujMmMS5KwVlLd_z7UMn5VjKDfhl4vLCcXYI8VcCgPPpMdY3wi-zl6u8-Vojgyg7ifpAoVqg9D2XqjhVXWgX5Y_Ce3fCxaOTnoknwaNsW9_ZeVN2uIbVV3WkPijc6xO1-V5Xs96i_xzoCbOHwBd5E_qNOVRywzfpda20lGAYbuBLKgUoQzgiakBKM-Kjye8UxzCexC8S28hdEbbjQjfccjEu5RWCPsc4oZlwqk2nZrQ9swA3LeNJCRcYWdbAv6_Gh49EMtXd8pgnKeLa2CSuLe2ZDRcjqtff1seymwAAAAHGI0sDAQ"
    
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
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Lisafans_bot")
                                  
