import requests


def fetch_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    if 'value' in data:
        return data['value']
    else:
        return "Failed to fetch Chuck Norris joke"


if __name__ == "__main__":
    joke = fetch_random_chuck_norris_joke()
    print(joke)




    """
    Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented 
    here: https://api.chucknorris.io/. The user should only be shown the joke text.
    """
