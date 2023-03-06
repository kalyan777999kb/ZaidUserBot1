import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25566413")) #optional
API_HASH = getenv("API_HASH", "5f4dcf21daeac7c01bb229e3e3349f3d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5655356960").split()))
OWNER_ID = int(getenv("OWNER_ID",  "5655356960"))
MONGO_URL = getenv("MONGO_URL",  "mongodb+srv://varmadivya:varmadivya@dividillu.dm5us5x.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5811227919:AAEMweZWcmHjmz3uh5PfNzl8ONtufwiRPq4")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/5e11fae6c913888a27c2b.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", )
PM_LOGGER = getenv("PM_LOGGER",  "True")
LOG_GROUP = getenv("LOG_GROUP",  "-1001642786913")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGGHM0AjFkLIe9NQxA9snTsWvuC_VaVd0vZKmQinLoQ4_zpTujiBhDgYLT0kt8YpSj2h2flezBMlje39JEQYIjjI6y7tE0aQl0ftP_OlxYaJAxz7Vrqxm1B0uxodsTf4rgXwmqhzkzfVkn-z__6Vw958U1iGXk8sHbUN31dgCQNHg1K4JmhRmbEpZSukrLLQj2qorfyT6CgLHgvcrTB3eh8GsizOLMCj2fRdZcTfQCw2GLs2nM4Shxrwp7sbn82YDJJrDWGg0lB9DkabBDkkHgohHm5J8pGt2GRBW2ipTZ8nr2G8rJyTdxDOZKLb0FtYnRLkgNg8rMYTuIR6XHLpPd6CTRgkAAAAAFRFeYgAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
