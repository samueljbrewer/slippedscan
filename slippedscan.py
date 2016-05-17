"""This program will go to the website slippedisc, get the html, search for
the stings "Boston", "Andris", and "Nelsons" and text me an alert if any of these
terms are on the page"""

import requests
from bs4 import BeautifulSoup
import smtplib

#this goes to the website and gets the html

url = 'http://slippedisc.com/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

headers = soup("h3")

slippedtext = open("slippedtext.txt", "r+")
lines = slippedtext.readlines()
last_title = lines[len(lines)-1]

for h in reversed(headers):
    if h == last_title.rstrip():
        pass
    else:
        slippedtext.write(str(h) + "\n")

slippedtext.close()

def filecheck():
    datafile = file("slippedtext.txt")
    found = []
    for text in datafile:
        if "Boston" in text or "Nelsons" in text or "Andris" in text or "Lockhart" in text or "BSO" in text or "John Williams" in text or "Women" in text:
            found.append(text)
    print found
    return found

def message():
    message = ""
    headlines = filecheck()
    for h in headlines:
        message += h + "\n"
    return message

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxbd78fb8b18124f3784b171f6f049ee61.mailgun.org/messages",
        auth=("api", "key-d453da24c7f7d4079c2862bebba466ee"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxbd78fb8b18124f3784b171f6f049ee61.mailgun.org>",
              "to": "Sam <samueljbrewer@gmail.com>",
              "subject": "slippedisc alert",
              "text": message()})

send_simple_message()
