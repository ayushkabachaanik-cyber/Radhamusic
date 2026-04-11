


from KanhaMusic.core.bot import Anu
from KanhaMusic.core.dir import dirr
from KanhaMusic.core.git import git
from KanhaMusic.core.userbot import Userbot
from KanhaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
#git()
dbb()
heroku()

app = Anu()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
