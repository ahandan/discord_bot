import pandas as pd
import requests
from bs4 import BeautifulSoup 




if __name__ == "__main__":
    url = 'https://reddit.nbabite.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    # table_MN = pd.read_html(page)
    competitions = soup.find(id='competitions')

    heure_matchs = soup.find_all("div", {"class": "status"})
    team_names = soup.find_all("div", {"class": "team-name"}) 

    # print(matches)
    match = {}

    for i, heure in enumerate(heure_matchs):
        s = heure.text + " : " +team_names[i+1].text + " @ " + team_names[i].text
        print(s)

            

    # for names in team_names:
    #     for name in names:
    #         match.extend(names)


    
    
    # print(mat)


    # print(competition.prettify())