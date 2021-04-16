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
'''
Здесь первая строка то что как раз ин адо
'/w/index.php?title=Online_chat&action=edit&section=5', '/wiki/Chat_room', '/wiki/Collaborative_software', '/wiki/Instant_messaging', '/wiki/Internet_forum', '/wiki/Online_dating_service', '/wiki/Real-time_text', '/wiki/Videotelephony', '/wiki/Voice_chat', 
'''