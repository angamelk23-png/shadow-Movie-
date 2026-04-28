from config import OWNER_ID
from stats import get_stats

async def admin(update,context):
 if update.effective_user.id!=OWNER_ID:
   return
 await update.message.reply_text(
 f'Admin\nSearches:{get_stats()}'
 )
