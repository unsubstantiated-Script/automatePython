import bs4, requests

res = requests.get('https://www.ebay.com/itm/335295163191')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elements = soup.select('.x-price-primary > span')

title = elements[0].text.strip()

print(title)
