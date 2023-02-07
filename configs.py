# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 22032175)
    API_HASH = os.environ.get("API_HASH", "54c21046170f78a2e099d10b8e791df6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6028539682:AAEc9f-yKrjMcPO3r3GZjNrneqQRNP_9ejQ")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "musicBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOHsBu7-H4fqzRe-i3LcictCMY0DxznfmLtuQeYGM8oK2YMVqC34zEEjYUWDGVxU6QeTMMdsjc1q4lrqPw5tK9oCiEiYdAgiOuFNgCj5tTa69677dQ9RLjxqcHcQVM1H4nfmYp6TKoYdhxz3DtzpgbzsIJ8aFr-CoF2lhg850_yiwjidnnan_QQLF9boKCOnjIf2T2Gh9OGawndlpXZmOxNIDl60Ma4lF8VdnSTBUS-adnP5XXOVTTF22U-uHw1ImO6-PShKQOQFAz8wFv2vTMaeQjb5JmIu1M2ociX6gRz-jdPVVfDlfXULqlB5nzD5FO4J8WOVEiOtLy-KufuhxWz5gPTs=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001890400490))
    BOT_USERNAME = os.environ.get("BOT_USERNAME") music5000_bot
    BOT_OWNER = int(os.environ.get("BOT_OWNER")) 5338589399
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001607474997)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/cyniteofficial'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/cyniteofficial'>Cynite</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/cyniteofficial'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Cyniteofficial</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Cyniteofficial</a></b>
"""


