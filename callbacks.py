from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from deep_links import build_pm_link
from config import BOT_USERNAME

async def callback_handler(update,context):
 q=update.callback_query
 await q.answer()
 d=q.data.split('_')
 owner=int(d[-1])

 if q.from_user.id!=owner:
  await q.message.reply_text('🫢 අනුගේ එවා බලන්න එපා හලෝ')
  return

 if d[0]=='quality':
   kb=[[InlineKeyboardButton(
   '📥 DOWNLOAD NOW',
   callback_data=f'dl_demo_{owner}'
   )]]
   await q.message.reply_text(
   'Quality Selected',
   reply_markup=InlineKeyboardMarkup(kb)
   )

 if d[0]=='dl':
   link=build_pm_link(BOT_USERNAME,'demo')
   await q.message.reply_text(f'Inbox 📩\n{link}')
