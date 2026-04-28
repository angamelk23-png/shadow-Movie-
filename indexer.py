from parser_utils import parse_caption
from database import add_file
from config import SOURCE_CHANNELS

async def channel_index(update,context):
 post=update.channel_post
 if post.chat.id not in SOURCE_CHANNELS:
  return

 raw=post.caption or getattr(post.document,'file_name','')
 parsed=parse_caption(raw)
 if not parsed:
  return

 parsed['file_id']=getattr(post.document,'file_id',str(post.message_id))
 parsed['channel_id']=post.chat.id
 parsed['message_id']=post.message_id

 await add_file(parsed)
