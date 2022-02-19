from typing import final
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


URL= "https://www.e-table.gr/restaurants/attiki.athina.kentroathinas"
#request page source from URL

def scraping_restaurants(url):
        r= requests.get(url)
        #print(r)
        soup = BeautifulSoup(r.content, "html.parser")
        #print(soup.prettify())
        scraped_rest= soup.find_all('div', class_= 'card__block')
        rest_names=[]
        final_names=[]
        names=[]
        for i in scraped_rest:
            restaurants= i.find_all('h5', class_='card__title')
            for i in restaurants:
                i = i.get_text().strip().replace('€', "")
                rest_names.append(i)
        for element in rest_names:
            final_names.append(element.strip())
        for i in final_names:
            names.append(i)
        
        dataframe= pd.DataFrame(names)

        locations=[]
        for i in scraped_rest:
            loc= i.find('small', {"class": "card__hashtag"})
            for i in loc:
                i = i.get_text().strip().replace('<small class="card__hashtag">', "")
                match = i.split(',')
                location= match[0]
                locations.append(location)
        
        dataframe2= pd.DataFrame(locations)

        frames = [dataframe, dataframe2]

        results = pd.concat(frames, axis=1)
        result= results.iloc[np.random.choice(results.index)]
        restaurant= result.iloc[0]
        location = result.iloc[1]

        return restaurant, location


        
#restaurant, location = scrap_restaurants(URL)
#print(restaurant, location)

URL_inf= 'https://food.allwomenstalk.com/cuisines-of-the-world/#1'

def scraping_information(url):
        r= requests.get(url)
        #print(r)
        soup = BeautifulSoup(r.content, "html.parser")
        #print(soup.prettify())
        scraped_rest= soup.find_all('div', class_= 'post p-4 overflow-hidden')
        information=[]
        infos=[]
        for i in scraped_rest:
            information.append(i.get_text())
        for i in information:
            infos.append([i])
        
        dataframe= pd.DataFrame(infos)
        dataframe = dataframe.drop([0,2,4,5,6,7,8,9,10,11,13,14,17,18,20], axis=0)
        dataframe.to_csv("cuisines.csv", index=False, encoding='utf8')



        

