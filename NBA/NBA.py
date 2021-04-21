import os, random
import requests
from bs4 import BeautifulSoup 



def NBA(args):
    print(args)
    args = args.split(' ')
    commands = {
        "help" : nba_help,
        "games" : getGames

    }
    commands = (commands.get(args[0], "getGames"))
    return commands(args[1:])

def getGames(args):
    url = 'https://reddit.nbabite.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    # table_MN = pd.read_html(page)
    competitions = soup.find(id='competitions')

    heure_matchs = soup.find_all("div", {"class": "status"})
    team_names = soup.find_all("div", {"class": "team-name"}) 
    date =  soup.find_all('div', {"class":"date d-sm-block d-none"})[0].text

    # print(matches)
    match = {}

    text = date + "\n"        

    for i, heure in enumerate(heure_matchs):
        s = heure.text + " : " +team_names[i+1].text + " @ " + team_names[i].text
        text += '\n' + s

    
    return to_text(text)


def nba_help(args):
    return "help"


def to_text(text:str):
    s = "```text\n"
    s += text +'\n'
    s += "```"
    return s