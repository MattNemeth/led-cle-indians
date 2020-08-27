# Import libraries
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import helpers
from helpers import splitter

#again = True
cnt = 0

#Makes loop infinite
while True:
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

    # data[17] = pitch count = 3 - 1 or 2 - 2
    balls =   int(data[17][0])
    strikes = int(data[17][4])
    outs =    int(data[16][0])
    innNum =  int(data[14][4])
    innTB =   str(data[14][0:3])
    
    helpers.displayInning(innNum, innTB) 
    helpers.displayStats(balls,strikes,outs)

    #opens .txt file for temp data storage
    file = open("output.txt","w")
    
    #clears contents of file
    file.truncate()
        
    for c, val in enumerate(data):
        print(str(c) +': ' + val)
        file.write(str(c) + ': ' + val + "\n")

    file.close()
    print(str(cnt) + ': Sleeping and searching again...')
    cnt += 1
    time.sleep(10)
    """
    again = input("Run again? (y/n)")
    if (again == 'y') or (again == 'Y'):
        again = True
    else:
        again = False
    """
