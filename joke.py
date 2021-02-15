import requests

def get_joke(word = "Any"):
    link = "https://v2.jokeapi.dev/joke/"+word #joke api
    response=((requests.get(link)).json())
    type_of_joke=response["type"]
    if type_of_joke=="twopart":
        try:
            setup = response["setup"]
            joke = response["delivery"]  # return joke 1line and 2line
            final_joke=setup+"\n"+"\n"+joke
            return final_joke
        except:
            print("API Not working")
    elif type_of_joke=='single':
        try:
            joke = response["joke"]
            return joke # return joke 1 liner
        except:
            print("API Not Working")
    else:
        setup=None
        error='Invalid command please try command "pls joke" for random or try command "pls joke type_of_joke"'
        return setup,error


def get_dad_joke():
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers).json()
    joke=response['joke']
    return joke
