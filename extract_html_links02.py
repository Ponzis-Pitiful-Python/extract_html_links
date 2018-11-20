#Original code
#https://stackoverflow.com/questions/27730041/how-to-extract-html-links-with-a-matching-word-from-a-website-using-python

#word search for web pages, outputs string word is in between
#"a href" and "p" tags - Ponzi

from bs4 import BeautifulSoup
import requests

url = input("Input url for search: ")
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

theWord = input("Input word you are searching for: ")

da_links = lambda tag: (getattr(tag, 'name', None) == 'a' and
                           'href' in tag.attrs and
                           theWord in tag.get_text().lower())

da_paragraph = lambda tag: (getattr(tag, 'name', None) == 'p' and
                           theWord in tag.get_text().lower())

results = soup.find_all(da_links)
results2 = soup.find_all(da_paragraph)

from pprint import pprint
pprint(results)
pprint(results2)