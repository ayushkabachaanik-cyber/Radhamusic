import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ✅ Time Conversion Utility
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# ✅ Basic Config
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
COOKIES = getenv("COOKIES", None)
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# ✅ Duration Config
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000"))

# ✅ Limits Conversion (after defining time_to_seconds)
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

# ✅ Owner & Bot Identity
LOGGER_ID = int(getenv("LOGGER_ID", "-1003774441740"))
OWNER_ID = int(getenv("OWNER_ID", "8441236350"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "II_YOUR_MADARA_DEFAULTER_II") 
BOT_USERNAME = getenv("BOT_USERNAME", "@gsiugeirbcodbsk_bot")

# ✅ Command Handler
COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

# ✅ Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ✅ Git & Upstream Repo
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Oyekanhaa/KanhaMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "")  # Only for private repo

# ✅ Support Links
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_kanhaa")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kanhaxduniya")


PLAYLIST_ID = "-1003474962530"



# Vars For API End Pont.
YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com') ## xBit Music Endpoint.
YT_API_KEY = getenv("YT_API_KEY" , 'xbit_H4kCLtcb03xrPVBA55khulZgqMKeT_8f' ) ## Your API key like: xbit_10000000xx0233 Get from  https://t.me/tgmusic_apibot



# ✅ Auto Features
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "500"))


# ✅ Spotify                              
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# ✅ Limits
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))

# ✅ String Sessions
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# ✅ Runtime Storage
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = []

# ✅ UI Images
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/5go4t6.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/ohezme.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
STATS_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ohezme.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/ohezme.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/ohezme.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ohezme.jpg"

# ✅ URL Validation
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is invalid. Must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is invalid. Must start with https://")
