# Import libraries
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import helpers
from helpers import splitter

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage

#again = True
cnt = 0
again = True

# Set the URL you want to webscrape from
url = 'https://www.mlb.com/indians/scores'
#url = 'espn.com/mlb/scoreboard'

class Client(QwebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
    
    def on_page_load(self):
        self.app.quit()

client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)
