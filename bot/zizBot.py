import os, random

import requests
from bs4 import BeautifulSoup 

class ziz() :

    def hello(self):
        print("---- Hello my name Ziz ----")

    def NBA(self):
        url = 'https://reddit.nbabite.com/'
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        # table_MN = pd.read_html(page)
        competitions = soup.find(id='competitions')

        heure_matchs = soup.find_all("div", {"class": "status"})
        team_names = soup.find_all("div", {"class": "team-name"}) 

        # print(matches)
        match = {}

        text = ""
        for i, heure in enumerate(heure_matchs):
            s = heure.text + " : " +team_names[i+1].text + " @ " + team_names[i].text
            text += '\n' + s

        
        return self.stringfy(text)

    def stringfy(self, text):
        s = "```text\n"
        s += text +'\n'
        s += "```"
        return s

    
