import requests
import bs4

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


def download_and_save_image(image_url, img_name):
    response = requests.get(f"{image_url}")
    file = open(f'E:\\count-color-inflags\\img\\{img_name}.png', 'wb') #fill in your own user path here
    file.write(response.content)
    file.close()


#test the functions
if __name__ == '__main__':

    html_soup = parse_page("https://en.wikipedia.org/wiki/File:Flag_of_Belarus.svg")

    url = get_image_url(html_soup)

    download_and_save_image(url, "Belarus")
