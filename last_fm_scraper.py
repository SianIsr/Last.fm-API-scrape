import os
from dotenv import find_dotenv, load_dotenv
import requests

# Load API keys and shared secret from environmental variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
SHARED_SECRET = os.getenv("SHARED_SECRET")

# Information to send requests to the server
api_root = "http://ws.audioscrobbler.com/2.0"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"

def get_task() -> str:
  valid_input = False

  while not valid_input:
    try:
      task = int(input("""
What exactly do you want to do?
1. Get friends
2. Get loved tracks
3. Get recent tracks
4. Get top albums
5. Get top artists
6. Get top tracks
7. Get top tags

Enter the corresponding number: """))
    except ValueError:
      print("\nError, type in a valid number and try again.")
      continue

    if task == 1:
      method = "getfriends"
      valid_input = True
    elif task == 2:
      method = "getlovedtracks"
      valid_input = True
    elif task == 3:
      method = "getrecenttracks"
      valid_input = True
    elif task == 4:
      method = "gettopalbums"
      valid_input = True
    elif task == 5:
      method = "gettopartists"
      valid_input = True
    elif task == 6:
      method = "gettoptracks"
      valid_input = True
    elif task == 7:
      method = "gettoptags"
      valid_input = True
    else:
      print("\nError. Enter a number from 1-7.")
      valid_input = False

  return method

# Information from the user for what kind of data to retrieve
username = input("Enter your username: ").strip()
method = get_task()

params = {
    "user": username,
    "api_key": API_KEY,
    "method": method
}

response = requests.get(api_root)
print(response.status_code)