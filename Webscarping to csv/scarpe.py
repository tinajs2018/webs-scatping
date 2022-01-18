from bs4 import BeautifulSoup
import requests
from csv import writer
url='https://www.property24.co.ke/property-for-sale-in-nairobi-c1890'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('div',class_="pull-left sc_listingTileContent")
with open('house.csv','w',encoding='utf8',newline='') as f:
    thewriter=writer(f)
    header=['Title','Location','Describition','Price']
    thewriter.writerow(header)
    
    for list in lists:
        title=list.find('div',class_="sc_listingTileAddress").text
        location=list.find('div',class_= "sc_listingTileAddress").text
        details=list.find('div', class_="sc_listingTileTeaser").text
        ksh= list.find('span').text
        info=[title,location,details,ksh]
        thewriter.writerow(info)
    
