from bs4 import BeautifulSoup
import requests


#  поиск раздела см. также
def find_see_also(data):
    if data.find('See also') != -1:
        while data.find('See also') != -1:
            pos = data.find('See also')
            data = data[pos + 8:]

        #  находить ссылки в этом промежутке и рабоатать с ними
        pos = data.find('^')
        data = data[:pos]
    else:
        data = 'Online_chat'
    return data


#  функция для проверки на мусорный ввод
def normalize_titles(cut_data):
    titles = cut_data.split('\n')
    chars = '!/.,:;\'\"?%^#@*&'

    for title in titles:
        if title == 'Edit' or title == '[edit]':
            titles.remove(title)

        flag = False

        for char in chars:
            if title.find(char) != -1:
                flag = True

        #  Иногда случается что этот элемент был удален ранее и вылазит ошибка
        try:
            if flag:
                titles.remove(title)
        except:
            pass

    for i in range(len(titles)):
        if titles[i].find('[edit]'):
            titles[i] = titles[i].replace('[edit]', '')

    try:
        while titles[-1] == '':
            titles.remove('')
    except:
        pass

    for title in titles:
        if len(title) > 80 or title == 'References':
            titles.remove(title)

    #  Вывод заголовков
    with open('outp.txt', 'a') as f:
        for title in titles:
            f.write(title + '\n')

    return titles


#  Парсим
def parsing(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


def duplicate_check(links, link):
    for checker in links:
        if link == checker:
            return False
    #  Если еще не брали
    return True


def main():
    links = []
    links.append('https://en.wikipedia.org/wiki/Online_chat')

    for link in links:
        soup = parsing(link)
        cutten_data = find_see_also(soup.text)

        #  Заголовки которые мы ищем
        titles = normalize_titles(cutten_data)

        for title in titles:
            link = 'https://en.wikipedia.org/wiki/' + title
            if duplicate_check(links, link):
                links.append(link)
                parsing(link)  # Рекусивный поиск ссылок

if __name__ == "__main__":
    main()

