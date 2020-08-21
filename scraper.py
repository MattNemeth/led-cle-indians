# Import libraries
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


again = True

#Makes loop infinite
while again:
    print("Test to see if it's doing anything")

    # Set the URL you want to webscrape from
    url = 'https://www.mlb.com/indians/scores'
    
    # Connect to the URL
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    
    #set html parsing
    page_soup = soup(page_html,"html.parser")

    #surely there is a better way to store this data or a better find all system
    #TODO: clean this up
    homeData_r   = page_soup.findAll("div",{"class":"sc-fzoxnE hSvLzT"})
    homeData_h_e = page_soup.findAll("div",{"class":"sc-fzoxnE EiGoQ"})
    awayData_r   = page_soup.findAll("div",{"class":"sc-fzoxnE cjJfrY"})
    awayData_h_e = page_soup.findAll("div",{"class":"sc-fzoxnE eSHmmv"})
    inningData   = page_soup.findAll("div",{"class":"sc-fzqAui eoGDzK"})
    playerData   = page_soup.findAll("div",{"class":"sc-fzqyvk cXvmPV"})
    countData    = page_soup.findAll("div",{"class":"sc-pscky ksGtdo"})
    outData      = page_soup.findAll("svg",{"class":"sc-oTNDV d1BCO"})

    # Runners onBase will be the trickiest. I can't grab a number or text
    # There is an "onBase" class that is set when there is a runner on base
    # I plan to find the parent element, step through each sibling and
    # detect which sibling has the "onBase" class and update based on which sibling
    # contained that data

    """
    onBaseData = page_soup.findAll("svg",{"class":"sc-pciEQ eEPsSY"})

    test1 = onBaseData[0].prettify()
    print("Test 1: ")
    print(test1)

    test2 = onBaseData[0].rect.next_sibling
    print("Test 2: ")
    print(test2)
    """

    inning =  inningData[0].text
    pitcher = playerData[0].text
    batter =  playerData[1].text
    count =   countData[0].text
    outs =    outData[0].text
    
    home_team_runs =   homeData_r[0].text
    home_team_hits =   homeData_h_e[0].text
    home_team_errors = homeData_h_e[1].text

    away_team_runs =   awayData_r[0].text
    away_team_hits =   awayData_h_e[0].text
    away_team_errors = awayData_h_e[1].text

    #opens .txt file for temp data storage
    file = open("output.txt","w")
    
    #clears contents of file
    file.truncate()

    file.write("Inning:  " + str(inning) + "\n")
    file.write("Pitcher: " + str(pitcher) + "\n")
    file.write("Batter:  " + str(batter) + "\n")
    file.write("Count:   " + str(count) + "\n")
    file.write("Outs:    " + str(outs) + "\n")

    file.write("Home Team Runs:   " + str(home_team_runs) + "\n")
    file.write("Home Team Hits:   " + str(home_team_hits) + "\n")
    file.write("Home Team Errors: " + str(home_team_errors) + "\n")

    file.write("Away Team Runs:   " + str(away_team_runs) + "\n")
    file.write("Away Team Hits:   " + str(away_team_hits) + "\n")
    file.write("Away Team Errors: " + str(away_team_errors) + "\n")

    file.close()

    again = input("Run again? (y/n)")
    if (again == 'y') or (again == 'Y'):
        again = True
    else:
        again = False

