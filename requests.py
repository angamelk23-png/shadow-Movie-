from database import requests_col

async def save_request(title,user):
 await requests_col.insert_one({
 'title':title,
 'user':user,
 'status':'pending'
 })
