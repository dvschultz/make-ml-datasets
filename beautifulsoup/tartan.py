import requests
from bs4 import BeautifulSoup
import string
from os import path

letters = list(string.ascii_uppercase)
subpages = []
img_links = []

#scrape index pages to get all subpages
for letter in letters:
	page = requests.get("https://www.tartanregister.gov.uk/az?searchString=%s" % letter)
	print(page.status_code)

	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup.prettify())

	links = soup.find_all("a")

	for link in links:
		if "tartanDetails.aspx" in link.get("href"):
			#print(link.get("href"))
			subpages.append(link.get("href").split("=")[1])

#scrape subpages

print(subpages)
# for subpage in subpages:
# 	page = requests.get("https://www.tartanregister.gov.uk/"+subpage)

# page = requests.get("https://www.tartanregister.gov.uk/tartanDetails.aspx?ref=10454")
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())


for subpage in subpages:
	filepath = './output/'+subpage+'.jpg'
	if (path.exists(filepath)):
		print(subpage + ' already exists')
	else:
		with open('./output/'+subpage+'.jpg', "wb") as f:
			f.write(requests.get("https://www.tartanregister.gov.uk/tartanImagePrototype?ref="+subpage+"&width=1024&height=1024&resize=no&shadows=yes&threadsize=4").content)