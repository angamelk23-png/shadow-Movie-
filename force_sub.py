from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from config import UPDATE_CHANNEL

async def subscribed(uid,bot):
 try:
   m=await bot.get_chat_member(UPDATE_CHANNEL,uid)
   return m.status in ['member','administrator','creator']
 except:
   return False

def join_markup():
 return InlineKeyboardMarkup([
 [InlineKeyboardButton('Join Channel',url='https://t.me/SHADOW_Movie23')]
 ])
