import requests
import random


def get_fact():
    # get random fact
    response = (requests.get("https://uselessfacts.jsph.pl/random.json?language=en")).json()
    fact = response['text']  # return fact in json Resources ['text'] to extract fact
    return fact  # return fact in 'str'


def get_random_number_fact():
    # facts about number
    list_of_options = ["year", "date", "trivia"]
    word = random.choice(list_of_options)  # randomly select form list
    final_link = "http://numbersapi.com/random/" + word + "?json"  # final link
    response = (requests.get(final_link)).json()
    fact = response['text']  # return fact in json Resources ['text'] to extract fact
    return fact  # return fact in 'str'


def get_number_fact(number):
    # facts about particular number
    list_of_options = ['/math', '/trivia']
    word = random.choice(list_of_options)
    final_link = "http://numbersapi.com/" + number + word + "?json"
    response = (requests.get(final_link)).json()
    fact = response['text']
    return fact  # return fact of number in str


def get_date_fact(date):
    # fact about particular date
    final_link = "http://numbersapi.com/" + date + "?json"
    response = (requests.get(final_link)).json()
    fact = response['text']
    return fact


def get_animals_fact():
    list_of_option = ['/dogs', '/cat', '/panda', '/fox', '/bird', '/koala']
    random_fact = random.choice(list_of_option)
    final_link = "https://some-random-api.ml/facts" + random_fact
    response = (requests.get(final_link)).json()
    fact = response['fact']
    return fact


def animal_fact(data):
    final_link = "https://some-random-api.ml/facts/" + data
    response = (requests.get(final_link)).json()
    fact = response['fact']
    return fact
