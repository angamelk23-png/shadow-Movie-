from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client=AsyncIOMotorClient(MONGO_URI)
db=client.moviehub

files=db.files
users=db.users
requests_col=db.requests

async def add_file(doc):
 await files.update_one(
  {"file_id":doc["file_id"]},
  {"$set":doc},
  upsert=True
 )

async def get_file(fid):
 return await files.find_one({"file_id":fid})

async def search_files(q):
 out=[]
 c=files.find({
  "normalized_title":{
   "$regex":q.lower()
  }
 }).limit(20)
 async for i in c:
  out.append(i)
 return out
