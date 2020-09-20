import requests
from bs4 import BeautifulSoup
import string
from os import path

subpages = [];
# # go thru each search page
for i in range(390,840,30):
	page = requests.get("https://www.dh-jac.net/db1/stencil/results.php?skip=" + str(i))
	# print(page.status_code)

	soup = BeautifulSoup(page.content, 'html.parser')
	# print(soup.prettify())

	links = soup.find_all("a", class_="thumbnail")
	# print(len(links))


	for link in links:
		# print(link.get("href"))
		subpages.append(link.get("href").split("=")[1])

# # print(subpages)
for subpage in subpages:
	# print(subpage)
	subpage = requests.get("https://www.dh-jac.net/db1/stencil/detail.php?accession_number=" + subpage)
	sp_soup = BeautifulSoup(subpage.content, 'html.parser')
	img_links = sp_soup.find_all("a", class_="image")
	# len(img_links)

	for img_link in img_links:
		# print(img_link)
		img = img_link.get("href")
		filename = img.split("/")[-1]
		# print(filename)
		filepath = './output/'+filename
		if (path.exists(filepath)):
			print(filename + ' already exists')
		else:
			with open(filepath, "wb") as f:
				f.write(requests.get(img).content)
