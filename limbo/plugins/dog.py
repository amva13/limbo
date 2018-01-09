"""!dog returns an image of a doggo or puppo."""
import re
import requests

def dog():
	# old dog picture code
    # return requests.get("https://dog.ceo/api/breeds/image/random").json()['message']

    # here's another dog!
    # return requests.get("http://www.what-dog.net/Images/faces2/scroll001.jpg").json()['message']
    return "https://www.what-dog.net/Images/faces2/scroll001.jpg"

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!dog( .*)?", text)
    if not match:
        return

    return dog()

on_bot_message = on_message
