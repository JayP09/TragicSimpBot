import requests
import random

def get_fact():
    
    #get random fact
    response=(requests.get("https://uselessfacts.jsph.pl/random.json?language=en")).json()
    fact = response['text'] #return fact in json data ['text'] to extract fact
    return fact #return fact in 'str'

def get_number_fact():
    #facts about number eg:date,year or any random number
    list_of_options = ["year","date","trivia"]
    word = random.choice(list_of_options) #randomly select form list
    final_link = "http://numbersapi.com/random/" + word +  "?json" #final link
    response=(requests.get(final_link)).json()
    fact = response['text']    #return fact in json data ['text'] to extract fact
    return fact #return fact in 'str'


def get_number_fact_2(number):
    final_link = "http://numbersapi.com/" + number + "?json"
    response=(requests.get(final_link)).json()
    fact = response['text']
    return fact #return fact of number in str