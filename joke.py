import requests
import urllib.request as url

def get_joke(word = "Any"):
    link = "https://v2.jokeapi.dev/joke/" + word #joke api

    try:
        return ((requests.get(link)).json())["delivery"],#return joke 1line and 2line
        print('2 liner')
    except :
<<<<<<< HEAD
        return ((requests.get(link)).json())["joke"]    #return joke 1 liner

def get_dad_joke():

=======
        return ((requests.get(link)).json())["joke"] #return joke 1 liner
        print('1 liner')

def get_dad_joke():
>>>>>>> be2a7d2ebc60d13887afe49ff9d752e490a870c9
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json()['joke']

