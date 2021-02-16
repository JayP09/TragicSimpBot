import requests
import urllib.request as url

def get_joke(word = "Any"):
    link = "https://v2.jokeapi.dev/joke/" + word #joke api

    try:
        setup = ((requests.get(link)).json())["setup"]
        joke = ((requests.get(link)).json())["delivery"]
        return setup, joke#return joke 1line and 2line
        
    except :
        return None,((requests.get(link)).json())["joke"] #return joke 1 liner
        

def get_dad_joke():
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json()['joke']

