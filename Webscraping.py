from bs4 import BeautifulSoup
import lxml 
import requests
from csv import writer

f = open('apartments.csv','a+', encoding='utf8',newline='')
thewriter=writer(f)
header=['Category', 'Floor', 'Bedrooms', 'Bathrooms', 'Area', 'Year', 'Price/m2(€/m^2)', 'Price(€)'] 
thewriter.writerow(header)

page=1
while page<64:
    url=f"https://www.xe.gr/property/results?page={page}&geo_place_ids%5B%5D=ChIJ7eAoFPQ4qBQRVARSDEXE8lI&item_type=re_residence&transaction_name=rent"
    page+=1
    data=requests.get(url)
    soup=BeautifulSoup(data.content, 'html.parser')
    lists=soup.find_all('div', class_="common-property-ad-body grid-y align-justify")

    for list_ in lists:
        try:
            space=list_.find('div', class_="common-property-ad-title").text.replace('\n','')
            price=list_.find('span', class_="property-ad-price").text.replace('\n','')
            price_m2=list_.find('span', class_="property-ad-price-per-sqm").text.replace('\n','')
            floor=list_.find("span", class_="property-ad-level").text.replace('\n','')
            bedrooms=list_.find("div", class_="grid-x property-ad-bedrooms-container").text.replace('\n','')
            bathrooms=list_.find("div", class_="grid-x property-ad-bathrooms-container").text.replace('\n','')
            area=list_.find("span", class_="common-property-ad-address").text.replace('\n','')
            year=list_.find("div", class_="grid-x property-ad-construction-year-container").text.replace('\n','')    
        except:
            space=None
            price=None
            price_m2=None
            floor=None
            bedrooms=None
            bathrooms=None
            area=None
            year=None
        info=[space,floor, bedrooms, bathrooms, area, year, price_m2, price]
        thewriter.writerow(info)