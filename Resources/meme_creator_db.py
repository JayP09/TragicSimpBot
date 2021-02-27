import re
import config

# database setup mongodb
client_obj = config.Database_oauth()
client = client_obj.database_info()
db = client["meme"]
collection = db["memedata"]
post = {}

# reddit 0auth
reddit = client_obj.oauth_info()


def meme_file_creator():
    collection.drop()
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



meme_file_creator()