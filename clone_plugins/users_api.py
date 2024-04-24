 
import requests
import json
from motor.motor_asyncio import AsyncIOMotorClient
from config import CLONE_DB_URI, DB_NAME
 
client = AsyncIOMotorClient(CLONE_DB_URI)
db = client[DB_NAME]
col = db["users"]
 
async def get_short_link(user, link):
    api_key = user["shortener_api"]
    base_site = user["base_site"]
    print(user)
    response = requests.get(f"https://{base_site}/api?api={api_key}&url={link}")
    data = response.json()
    if data["status"] == "success" or rget.status_code == 200:
        return data["shortenedUrl"]
 
async def get_user(user_id):

    user_id = int(user_id)

    user = await col.find_one({"user_id": user_id})

    if not user:
        res = {
            "user_id": user_id,
            "shortener_api": None,
            "base_site": None,
        }

        await col.insert_one(res)
        user = await col.find_one({"user_id": user_id})

    return user
 
async def update_user_info(user_id, value:dict):
    user_id = int(user_id)
    myquery = {"user_id": user_id}
    newvalues = { "$set": value }
    await col.update_one(myquery, newvalues)
 
async def total_users_count():
    count = await col.count_documents({})
    return count
 
async def get_all_users():
    all_users = col.find({})
    return all_users
 
async def delete_user(user_id):
    await col.delete_one({'user_id': int(user_id)})

 
