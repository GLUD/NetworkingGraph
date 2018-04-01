# https://www.dataquest.io/blog/web-scraping-tutorial-python/
import requests
from bs4 import BeautifulSoup

# Ejemplo con etiquetas

page = requests.get(
    "http://dataquestio.github.io/web-scraping-pages/simple.html")
page
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# print(soup.prettify())
# print(list(soup.children))
#print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
# print(list(html.children))
body = list(html.children)[3]
# print(list(body.children))
p = list(body.children)[1]
# print(p.get_text())

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('p'))
# print(soup.find_all('p')[0].get_text())


# Ejemplo con clasesy IDs

page = requests.get(
    "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup
# print(soup.find_all('p', class_='outer-text')) # busca texto interno
# print(soup.find_all(class_="outer-text"))
# print(soup.find_all(id="first"))

# Usando selectores class

#print(soup.select("div p"))

# Realizando web scraping a una pagina de pronostico del clima

page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())

'''
    The name of the forecast item — in this case, Tonight.
    The description of the conditions — this is stored in the title property of img.
    A short description of the conditions — in this case, Mostly Clear.
    The temperature low — in this case, 49 degrees.
'''

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

'''print(period)
print(short_desc)
print(temp)
'''
img = tonight.find("img")
desc = img['title']

# print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)
short_descs = [sd.get_text()
               for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# print(short_descs)
# print(temps)
# print(descs)
import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
#print(weather)
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
#print(temp_nums)
#print(weather["temp_num"].mean())
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
#print(is_night)
print(weather[is_night])
