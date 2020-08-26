# Import libraries
from time import sleep
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from gpiozero import LED, Button

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

    
    led = LED(26)
    
    cnt = 0
    
    while cnt < 5:
        led.on()
        print('on')
        sleep(1)
        led.off()
        print('off')
        sleep(1)
        cnt += 1    

    #opens .txt file for temp data storage
    file = open("output.txt","w")
    
    #clears contents of file
    file.truncate()
        
    for i in data:
        print(i)
        file.write(str(i) + "\n")

    file.close()

    again = input("Run again? (y/n)")
    if (again == 'y') or (again == 'Y'):
        again = True
    else:
        again = False

