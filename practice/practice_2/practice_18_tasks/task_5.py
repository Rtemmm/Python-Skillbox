import requests
from bs4 import BeautifulSoup


def get_h3_tags(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h3_tags = soup.find_all('h3')
    return [tag.text for tag in h3_tags]


url = 'http://www.columbia.edu/~fdc/sample.html'
print(get_h3_tags(url))
