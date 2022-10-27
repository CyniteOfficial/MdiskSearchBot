# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", “11484651”))
    API_HASH = os.environ.get("API_HASH", "9d058bf3591ddba2870ea61836571eae")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5765769840:AAF3X6xQ6Hr15CR6rk4pG4Ymi2VaeVO14T0")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001144412978))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/IPopcornSearch_bot'>I Popcorn Search Movie Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/Jayesh_Rajput1'>Jayesh</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/Jayesh_Rajput1'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm I Popcorn Search Movie Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Jayesh_Rajput1</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm I Popcorn Search Movie Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Jayesh_Rajput1</a></b>
"""


