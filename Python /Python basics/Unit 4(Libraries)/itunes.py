import json
import requests
import sys

if len(sys.argv) != 2:
	print("Usage: python itunes.py <search_term>")
	sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
	print(result["trackName"])