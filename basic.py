import requests
"""
url = "http://ku.edu.np"
r = requests.get(url)
print(r.status_code)
print(r.text)
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
soup = BeautifulSoup(page, "html.parser")
""""
city_list = soup.find_all( "td", class_="city" )
for city in city_list:
    print( city.getText() )
"""

#phone_number = soup.find(id="call")
#print(phone_number.text)

image_list = soup.find_all('img')
for image in image_list:
    print(image.attrs['src'])
    
    
#just adding comment    