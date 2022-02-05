import requests
from bs4 import BeautifulSoup
from collections import Counter
from tabulate import tabulate


def start(url):
    worldlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'lxml')

    for each_text in soup.findAll('p')[6:36]:
        content = each_text.text
        words = content.lower().split()
        for each_word in words:
            worldlist.append(each_word)
        clean_wordlist(worldlist)
    return worldlist


def clean_wordlist(worldlist):
    clean_list = []
    for word in worldlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_list.append(word)
    create_dict(clean_list)
    return clean_list


def create_dict(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    c = Counter(word_count)
    top = c.most_common(10)
    return top
    print(top)

if __name__ == '__main__':

    url = "https://en.wikipedia.org/wiki/Microsoft"

    worldlist = start(url)
    good_list = clean_wordlist(worldlist)
    top_list = create_dict(good_list)
    # print(start(url))
    # print(clean_wordlist(worldlist))
    # print(create_dict(worldlist))
    # print(top_list)

    headers = ["", "# of occurrences"]
    table = top_list
    print(tabulate(table, headers, tablefmt="fancy_grid"))
