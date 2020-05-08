import requests
from bs4 import BeautifulSoup as soup
import json


def get_user_info(user_url):
    # url = "https://stackoverflow.com/users/8608146/phani-rithvij"
    # url = "https://stackoverflow.com/users/22656/jon-skeet"
    if not user_url.startswith("https://stackoverflow.com/users/"):
        raise ValueError("Not a valid url")
    tabsurl = user_url + "?tab=tags&sort=votes&page={}"

    curr = 0

    with open("out.json", 'w+') as out:
        data = {}
        while True:
            curr += 1
            r = requests.get(tabsurl.format(curr))
            html = soup(r.content, features='lxml')
            table = html.find('table', {'class': 'user-tags'})
            tagurls = table.find_all('td')
            if len(tagurls) == 0 or curr == 20: #here
                break
            for tag in tagurls:
                count = ''
                try:
                    count = tag.div['title'].split(' ')[-1][:-1]
                    count = int(count)
                except:
                    count: str = tag.div.text
                    count = count.replace('k', '000')
                    try:
                        count = int(count)
                    except Exception as e:
                        print(e)
                # count can be 0 increase the frequency
                count += 1
                data[tag.a.text] = count
                # print(tag.div.text, count, tag.a.text)
                # if cou
            print("{}/{}".format(count, 20))
        json.dump(data, out)
