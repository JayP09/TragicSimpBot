import pymongo
import praw
import re
from prawcore import NotFound
from Resources import config
# database setup mongodb
client_obj = config.Database_oauth()
client = client_obj.database_info()
db = client["meme"]
collection = db["memedata"]
post = {}

# reddit 0auth
reddit = client_obj.oauth_info()

def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists


def meme_file_creator():
    page_list = ['funny', 'dankmemes', 'memes', 'teenagers', 'Chodi', "DsyncTV", 'cursedcomments', 'holdup',
                 'SaimanSays/', 'wholesomememes', 'IndianMeyMeys', 'indiameme', 'desimemes', 'Tinder', '2meirl4meirl',
                 'ComedyCemetery', 'terriblefacebookmemes']
    # field = ['MemePage', 'Memetitle', 'MemeUrl']
    j = 1
    for meme_page in page_list:
        memes = reddit.subreddit(meme_page)
        top_memes = memes.top('week')
        i = 0  # counter for selecting 5 memes
        for memes in top_memes:
            if re.search("^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg)$", memes.url):
                post = {"_id": j, "memepage": meme_page, "memetitle": memes.title, "memeurl": memes.url, "count": 0}
                collection.insert_one(post)
                i, j = i + 1, j + 1
            if i == 5:
                break  # number of memes per page
    print('done')


def single_meme(page):
    if sub_exists(page):
        page_data = reddit.subreddit(page)
        post = page_data.new()
        print(post)
        for posts in post:
            if re.search("^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg)$", posts.url):
                memepage, memetitle, memeurl = page, posts.title, posts.url
                return memepage, memetitle, memeurl  # return Resources
            elif re.search("^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:gif)$", posts.url):
                memepage, memetitle, memeurl = page, posts.title, posts.url
                return memepage, memetitle, memeurl  # return Resources
            else:
                continue
    else:
        memepage, memetitle, memeurl = None, 'Failed', 'https://media.giphy.com/media/HNEmXQz7A0lDq/giphy.gif'
        return memepage, memetitle, memeurl
