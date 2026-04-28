import requests
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import *

from config import *
from callbacks import callback_handler
from force_sub import subscribed,join_markup
from indexer import channel_index
from admin import admin
from stats import add_search
from requests import save_request


def tmdb_search(query):
 url=(
 f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_KEY}&query={query}'
 )
 data=requests.get(url).json()
 if not data['results']:
   return None
 m=data['results'][0]
 return {
 'title':m['title'],
 'poster':'https://image.tmdb.org/t/p/w500'+m['poster_path'],
 'overview':m['overview'],
 'rating':m['vote_average']
 }

async def start(update,context):
 if context.args:
   await update.message.reply_text('🎬 Download Ready')
   return

 await update.message.reply_text('''
╔══════════════════════╗
🎬 WELCOME TO MOVIE HUB
╚══════════════════════╝

Type movie name in group 🍿
''')

async def request_cmd(update,context):
 title=' '.join(context.args)
 await save_request(title,update.effective_user.id)
 await update.message.reply_text('Request saved')

async def auto_filter(update,context):
 ok=await subscribed(
 update.effective_user.id,
 context.bot
 )
 if not ok:
   await update.message.reply_text(
   'Join first',
   reply_markup=join_markup()
   )
   return

 add_search()
 movie=tmdb_search(update.message.text)
 if not movie:
   await update.message.reply_text('Movie not found')
   return

 cap=f'''🎬 {movie['title']}
⭐ {movie['rating']}

{movie['overview'][:180]}...'''

 kb=[
 [
 InlineKeyboardButton(
 '1080p',
 callback_data=f'quality_1080_{update.effective_user.id}'
 ),
 InlineKeyboardButton(
 '720p',
 callback_data=f'quality_720_{update.effective_user.id}'
 )
 ],
 [InlineKeyboardButton(
 '🎞 Trailer',
 url='https://youtube.com'
 )]
 ]

 await update.message.reply_photo(
 photo=movie['poster'],
 caption=cap,
 reply_markup=InlineKeyboardMarkup(kb)
 )

def main():
 app=ApplicationBuilder().token(BOT_TOKEN).build()

 app.add_handler(CommandHandler('start',start))
 app.add_handler(CommandHandler('request',request_cmd))
 app.add_handler(CommandHandler('admin',admin))
 app.add_handler(CallbackQueryHandler(callback_handler))
 app.add_handler(
 MessageHandler(
 filters.TEXT & ~filters.COMMAND,
 auto_filter
 ))
 app.add_handler(
 MessageHandler(
 filters.UpdateType.CHANNEL_POST,
 channel_index
 ))

 app.run_polling()

if __name__=='__main__':
 main()
