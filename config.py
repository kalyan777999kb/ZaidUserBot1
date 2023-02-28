import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25566413")) #optional
API_HASH = getenv("API_HASH", "5f4dcf21daeac7c01bb229e3e3349f3d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5655356960").split()))
OWNER_ID = int(getenv("OWNER_ID",  "5655356960"))
MONGO_URL = getenv("MONGO_URL",  "mongodb+srv://king777:kalyan@cluster0.zco8nze.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5811227919:AAEMweZWcmHjmz3uh5PfNzl8ONtufwiRPq4")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAmEZ3uFNopNhj7eklZVk8-U2S2Jm2gUgFZqDOeA4vQ_WA_9Cyb_HVbt31fp9JS9qBI9tj8boJuA_tUndhbQRIteaw4iPo2qSkeX-R6Z7IRiKdu0zX9qod8EF8Ojt7FtgPgRWWOiqUM0hRm32PNnBje_V6GfJNUrq0P2v3zYXzXZDhPEoJypyUAox7WbFtBUrkeQIaDrGJHNcevQYCWJKtbr6eylPrg6vWgIFbs75c2jrVuEstHq_BVAtEbB2NoPW5WwcWnolsYD8aJnp84iGLnxL04IddLRBBA1qNpRl67GKaY69_lPDIbXJMd0EyGZhQ0mUR6w521wmkJhv68bRxjwAAAAFRFeYgAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
