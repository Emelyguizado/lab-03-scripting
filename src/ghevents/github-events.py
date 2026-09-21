#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
	"Download data/events from the url and return them as Python objects"
	text = requests.get(url).text
	data = json.loads(text)
	return data


def print_events(events, n=5):
	"printing the first 5 event's type and repo"
	for x in events[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)

def main():
	"prints value of GHUSER and of url and runs only when the file is executed directly"
	print(GHUSER)
	print(url)
	events = retrieve_events(url)
	print_events(events)

if __name__ == "__main__":
    main()
