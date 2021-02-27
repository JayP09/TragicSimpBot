import random
import pymongo
from Resources import config
from prawcore import NotFound
import re

client_obj = config.Database_oauth()
client = client_obj.database_info()
db = client["meme"]
collection = db["memedata"]
reddit = client_obj.oauth_info()

max_count = list(collection.find().sort("count", -1).limit(1))[0]['count']  # get max count


def send_meme(x=0):
    total_memes = collection.estimated_document_count()  # total_meme
    random_number = random.randint(1, total_memes)  # random meme by id
    meme_data = collection.find_one({"_id": random_number})  # cursor object to list
    if x == 0:
        if meme_data['count'] == max_count:
            send_meme(x=1)  # just increase the probability of not getting same meme by 1/(totalmeme)**2
        else:
            collection.update_one({"_id": random_number}, {"$set": {"count": meme_data['count'] + 1}})  # update count
            memepage, memetitle, memeurl = meme_data['memepage'], meme_data['memetitle'], meme_data['memeurl']
            return memepage, memetitle, memeurl  # return Resources
    else:
        collection.update_one({"_id": random_number}, {"$set": {"count": meme_data['count'] + 1}})  # update count
        memepage, memetitle, memeurl = meme_data['memepage'], meme_data['memetitle'], meme_data['memeurl']
        return memepage, memetitle, memeurl  # return Resources


def send_specific_meme(memepage):
    data = collection.find({"memepage": memepage})
    count = data.count()
    # id = data[0]['_id']
    # random_number = random.randint(id,count+id-1)
    random_num = random.randint(0, count - 1)
    meme_data = data[random_num]
    memepage, memetitle, memeurl = meme_data['memepage'], meme_data['memetitle'], meme_data['memeurl']
    return memepage, memetitle, memeurl


def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists


def single_meme(page):
    if sub_exists(page):
        page_data = reddit.subreddit(page)
        post = page_data.hot()
        for posts in post:
            if re.search("^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif)$", posts.url):
                memepage, memetitle, memeurl = page, posts.title, posts.url
                return memepage, memetitle, memeurl  # return Resources
    else:
        memepage, memetitle, memeurl = None, 'Failed', 'https://media.giphy.com/media/HNEmXQz7A0lDq/giphy.gif'
        return memepage, memetitle, memeurl
