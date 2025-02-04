import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7333760658:AAHma51n_VYMCl9Gpt2Ak0sWTsx3GmkSgkw")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "15047947"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8e95af19215c497a2e8799ef7c6fa969")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5676436259"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
