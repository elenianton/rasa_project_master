from url import scraping_restaurants
import pandas as pd

URL= "https://www.e-table.gr/restaurants/attiki.athina.kentroathinas"

#res = scraping_restaurants(URL)
#print(res)

heleni= [['eleni', URL]]
df= pd.DataFrame(heleni, columns = ['Name', 'Age'])
csv= df.to_csv("links")
df.set_index("Name", inplace=True)

with open("C:\Users\eleni\Desktop\rasa_project\actions\links", 'r') as file:
    url= file.at['eleni','Age']
    print(url)