# Import libraries
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

from helpers import splitter

again = True

#Makes loop infinite
while again:
    # Set the URL you want to webscrape from
    url = 'https://www.mlb.com/indians/scores'
    
    # Connect to the URL
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    
    #set html parsing
    page_soup = soup(page_html,"html.parser")
    data = page_soup.find('div',{'data-test-mlb':'singleGameContainer'})

    #get_text not availible if data is a list of tags
    #future proof thinking for having data for any live game
    data = data.get_text('|', strip=True)

    data = splitter(data)
    print(data)

    #opens .txt file for temp data storage
    file = open("output.txt","w")
    
    #clears contents of file
    file.truncate()
        
    for i in data:
        file.write(str(i) + "\n")

    file.close()

    again = input("Run again? (y/n)")
    if (again == 'y') or (again == 'Y'):
        again = True
    else:
        again = False

