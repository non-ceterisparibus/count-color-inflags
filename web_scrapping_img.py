import requests
import bs4
import os

from download_img import *

cwd = os.getcwd()
#send a request to wikipedia website with a list of all states
url = 'https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags'
nurl = 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'
wikiURL = 'https://en.wikipedia.org/'
soup = parse_page(url)

for country in soup.find_all('div', class_='thumb'):
    country_name = country.div.a['title']
    print('Flag:' + country_name)
    fullImgLink = wikiURL + country.div.a['href']
    soup_img = parse_page(fullImgLink)
    image_url = get_image_url(soup_img)
    download_and_save_image(f"{image_url}", country_name, cwd)


print('Done')