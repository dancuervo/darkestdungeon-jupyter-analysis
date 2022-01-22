# import darkestdungeon heroes stats as sheet
import requests

p = "https://darkestdungeon.fandom.com/wiki/Heroes_(Darkest_Dungeon)"

raw_data = requests.get(p)

f = open("./files/heroes.txt", "w")
f.write(raw_data.text)
f.close()