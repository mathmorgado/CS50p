import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
json_response = response.json()

for song in json_response["results"]:
    print(song["trackName"])


