import re
from colorama import Fore
import requests
from bs4 import BeautifulSoup

website = "https://www.vulnhub.com"
result= requests.get(website)
content = result.text



###Method 2 using BeautifulSoup
print("METHOD 2 using BS4")

maquinas_final=[]


content = BeautifulSoup(result.content, 'html.parser')
tag_titles=content.select(".card-title > a")


for t in tag_titles:
    maquinas_final.append(t.string.strip())

############
# hardcoded example called "Noob: 1"
# we'll assume such object already existed in the Database as the last entry of the first page of machines, 
# and we'll iterate the new list of machines
# if such machine is not on the list, we'll assume there was a new entry, moving our harcoded example to the second page

maquina_noob="Noob: 1"
existe_noob=False

for i in maquinas_final:
    print(i)
    
for a in maquinas_final:
    if a == maquina_noob:
        existe_noob=True
        break
    
if existe_noob:
    print("There was not a new entry")
else:
    print("There IS a new entry")
    