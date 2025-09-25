import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Here's a joke!")
        print(f"{data['setup']}")
        print(f"{data['punchline']}")
    else:
        print(f"Error: {response.status_code}. Could not fetch a joke at this time.")

if __name__ == '__main__':
    get_joke()