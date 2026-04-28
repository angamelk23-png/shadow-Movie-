import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN=os.getenv('BOT_TOKEN')
TMDB_KEY=os.getenv('TMDB_KEY')
MONGO_URI=os.getenv('MONGO_URI')
BOT_USERNAME=os.getenv('BOT_USERNAME')
OWNER_ID=int(os.getenv('OWNER_ID'))
REDIS_URL=os.getenv('REDIS_URL')
UPDATE_CHANNEL=os.getenv('UPDATE_CHANNEL')

SOURCE_CHANNELS=[
-1001111111111,
-1002222222222,
]
