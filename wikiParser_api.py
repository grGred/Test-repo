import requests, json
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/w/api.php?action=parse&page=Online_chat&sectiontitle=See%20also&format=json'

response = requests.get(url)
json_data = json.loads(response.text)

text = str(json_data['parse']['text'])

pos = text.find('<span class="mw-headline" id="See_also">See also</span>')
text = text[pos+1:]

pos = text.find('</ul')
print(text[:pos])
soup = BeautifulSoup(text, 'html.parser')
print()

print(soup)
print()

a = []
for possible_link in soup.find_all('a'):
    a.append(str(possible_link.get('href')))
print(a)
