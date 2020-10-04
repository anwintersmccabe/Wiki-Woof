
import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

#takes in a search query and creates a text file of all the wikipedia image urls associated with it
def find_imgs(query):
    url = 'https://en.wikipedia.org/wiki/'
    newurl= url+query
    try:
        html = urlopen(newurl)
    except:
        print("nah bro try again")
        query = input("enter another page to search for: ")
        find_imgs(query)
    else:
        soup = BeautifulSoup(html, 'html.parser')
        f = open("image_urls.txt","w")
        urls = soup.find_all('a', class_="image")
        for x in urls:
            urlstr = str(x)
            urlstr = urlstr[22:]
            endIndex = urlstr.find('>')
            urlstr = urlstr[:endIndex]
            print(urlstr)
            f.write(urlstr+"\n")
        f.close()
    
query = input("Enter a page to search for: ")
find_imgs(query)







