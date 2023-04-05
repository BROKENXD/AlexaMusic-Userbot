import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "21124451"))
API_HASH = os.getenv("API_HASH", "d0c75e0e8ae1f79ddad10a033411f9ed")
SESSION = os.getenv("SESSION", "BQCJ5Z8QiwpNaOU-_sEp_yJow33i4PPfuP9MyMaZpP8wJBacP6ZFkW5f_9oe0WmQnZl-3FZOyGVcRn3gnmNeHs6nvtsQfM5t4KseoA0rJLL8ewm6E3EzMtEj4QAhf_3UwHUNTR7BGzFpob2C8_xRl_RrbIdNBdzx1vRCx0OwTOmr-fIZrOMhos17HEdntfg9C6W50m211QSaXhCfdBEm3kKGu38mjGqMkyt-oiUXKeHiy-zC1aOIoDNZnhuYqx5-1GYsCVw6ALLYh5WivUW_3c6pBDnMLU0Mv2UOXju-eznS9YSDEWEPYEn1-55ZShiz2UPlucyTkKQzkMvGwpUoI-BFAAAAAWTX6CIA")
HNDLR = os.getenv("HNDLR", "/")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AsadAlexaVCBot"))
call_py = PyTgCalls(bot)
