from datetime import timedelta
import pandas as pd
import random
import meme_creator
meme_list = pd.read_csv('discfactbot/memeofweek.csv')

def send_meme(rows):
    row_number = random.randint(0,rows)
    number , page, title ,url ,count = meme_list.loc[row_number]
    return page,title,url,row_number

def meme_main():
    rows,column = meme_list.shape
    if rows == 0 :
        meme_creator.meme_file_creator()
    else:
        page , title, url ,row_number = send_meme(rows)
        meme_list.drop(row_number,inplace= True)
        meme_list.to_csv('discfactbot/memeofweek.csv',index=False , sep=',')
        return page,title,url
