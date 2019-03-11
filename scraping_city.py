import requests,pprint
from bs4 import BeautifulSoup
url="http://www.census2011.co.in/data/subdistrict/4953-jangareddigudem-west-godavari-andhra-pradesh.html"
dawnlod=requests.get(url)
# print(dawnlod.text)
soup=BeautifulSoup(dawnlod.text,"html.parser")
# print(suop)
def city_list():
	data_list=[]
	http='http://www.census2011.co.in'
	div=soup.find("div",class_='table-responsive')
	# return(div)

	city_table=div.find("table",class_='table table-striped table-hover')
	body=city_table.find("tbody")
	data_tr=city_table.find_all('tr',class_='tr1')
	for tr in data_tr:
		convat_list=tr.text.strip().split("\n")
		# print(convat_list[3])
		city_link=tr.find("td",class_='alignleft')
		link=city_link.find('a').get('href')
		movie_details={'No':'','Villages':'','Administrative_Division':'','Population':'','url':''}

		movie_details['No']=convat_list[0]
		movie_details['Villages']=convat_list[1]
		movie_details['Administrative_Division']=convat_list[2]
		movie_details['Population']=convat_list[3]
		movie_details['url']=http+link
		pprint.pprint(movie_details)

		print('------------------------------------------------------------------------------')


sho=city_list()
print (sho)