import requests
from bs4 import BeautifulSoup
from collections import Counter
from tabulate import tabulate
from tkinter import *


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

# class Table:
	
# 	def __init__(self,root):
		
# 		# code for creating table
# 		for i in range(total_rows):
# 			for j in range(total_columns):
				
# 				self.e = Entry(root, width=20, fg='blue',
# 							font=('Arial',16,'bold'))
				
# 				self.e.grid(row=i, column=j)
# 				self.e.insert(END, lst[i][j])
# # take the data
# lst = top_list

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
class Table:
	
	def __init__(self,root):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(root, width=20, fg='blue',
							font=('Arial',16,'bold'))
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])
# take the data
lst = top_list

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()
