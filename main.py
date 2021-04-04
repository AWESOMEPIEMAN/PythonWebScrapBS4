import requests
import bs4

res = requests.get('Website link')

print(type(res))
soup = bs4.BeautifulSoup(res.text, 'lxml')

h = soup.select('h1')
print(type(h))
print(h)
