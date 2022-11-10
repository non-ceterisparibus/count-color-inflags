import requests
import bs4
import os
cwd = os.getcwd()

def parse_page(url):
    response = requests.get(url)
    #print(response)
    text = response.text
    soup = bs4.BeautifulSoup(text, "lxml")
    return soup


def get_image_url(soup):
    image = soup.find('div', class_='fullImageLink')
    image_url = f"https:{image.img['src']}"
    return image_url


def download_and_save_image(image_url, img_name, cwd):
    response = requests.get(f"{image_url}")
    file = open(f'{cwd}\\img\\{img_name}.png', 'wb')
    file.write(response.content)
    file.close()


#test the functions
if __name__ == '__main__':

    html_soup = parse_page("https://en.wikipedia.org/wiki/File:Flag_of_Bangladesh.svg")

    image_url = get_image_url(html_soup)
    print(image_url)

    download_and_save_image(image_url, "Bangladesh", cwd)
