# import requests
# from bs4 import BeautifulSoup

# response = requests.get(
#     url = "https://en.wikipedia.org/wiki/Web_scraping",
# )

# soup = BeautifulSoup(response.content, 'html.parser')
# title = soup.find(id="firstHeading")
# print(title.string)
# print(response.status_code)

import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f'<<<<<<<<<< {title} >>>>>>>>>> \nDo you want to view it ? (y/n)')
    print("\nSay y if you are a regular reader and you are interested. . .")
    print("\nsay n if you are not interested in the topic but you wanna read something else. . .")
    print("\nsay anything if you don't give a **** about what's going onn here. . . ")
    ans = input()

    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "n":
        print("\n>>>>>>we are searching another one for you. . .")
        continue
    else:
        print("\n >>>>>>>OKKKHHH so you don't give a ****.\nThat is what 70 percent of people do. . .\nSee, you are not alone but you are probably a VIBE KILLER. . .")
        break