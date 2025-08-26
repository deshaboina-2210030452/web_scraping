import requests
from bs4 import BeautifulSoup

def get_article_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch the page.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    
    title = soup.find('h1')
    date = soup.find('time')
    paragraphs = soup.find_all('p')

    print("\nð° Title:")
    print(title.get_text(strip=True) if title else "Not found")

    print("\nð Date:")
    print(date.get_text(strip=True) if date else "Not found")

    print("\nð Article Content:")
    for para in paragraphs:
        text = para.get_text(strip=True)
        if text:
            print(text)

# Sample usage
if __name__ == "__main__":
    url = 'https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html'
    get_article_content(url)
