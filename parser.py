from os import write
from bs4 import BeautifulSoup
import csv

#lee archivo y lo paresea en BeatifulSoup
file = "./files/heroes_stats.html"
with open(file) as fp:
    soup = BeautifulSoup(fp,"html.parser")

#crea una lista con los elementos th del html
fields = soup.find_all("th")
#crea una lista vacia para recibir el contenido de los th
headers_table = []
#crea una lista en que cada elemento es una lista de un elemento...
i = 1
while i < len(fields):
    headers_table.append(fields[i].text.split())
    i += 1
#crea una nueva lista vacia y le agrega el primer elemento de headers_table
#creando una lista de strings
headers_stats = []
for i in headers_table:
    headers_stats.append(i[0])

lineas_de_stats = soup.find_all("tr")
stats_list = []


i = 2
while i < len(lineas_de_stats):
    stats_list.append(lineas_de_stats[i].text.split())
    i += 1

with open('./files/hero_stats.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(headers_stats)
    write.writerows(stats_list)


print(f'Header len:\t {len(headers_stats)}')
i = 0
while i < len(stats_list):
    print(f'Row [{i}]len:\t {len(stats_list[i])}')
    i += 1