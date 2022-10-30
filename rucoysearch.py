from bs4 import BeautifulSoup
import requests


while True:
    player_name = input('Enter player name : ')
    url = 'https://www.rucoyonline.com/characters/' + player_name 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_ = 'character-table table table-bordered')
    print("\n".join([s.strip() for s in table.get_text().split("\n") if s]))



     
