Steps to success

1. Find a website to scrape from that the url doesnt change: mlb.com/indians/scores looks promising
2. Scrape the correct data
3. Get raspi setup with the working script
4. Build breadboard led field and have all the data about the game
    Balls/strikes
    outs
    score
    baserunners
    number of player at bat
    inning top/bottom
5. Connect raspi to the led field and update the field based on the data that was scraped from the website
6. Once everything is working THEN worry about making it nice. KISS


Issues: Can correctly grab data about the game when the html source reflects game data. If elements are updated with JS after the page loads I'm unable to get the data I want. Will need to transition to a headless browser capable of executing this JS and then grabbing the newly populated data. 

I believe selenium and headless firefox will be able to do what I want. Was having too many issues installing PyQt5 so I'm not going to move forward with it.

While this is a setback this will give me time to design the LED matrix and properly implement it. Once I get the scraper grabbing data with JS I may try and have all of it scroll across an oled display.
