import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get("https://forecast.weather.gov/MapClick.php?textField1=38.89&textField2=-77.03")
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')
# print(items[0])

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
# print(period_names)
# print(short_descriptions)
# print(temperatures)

weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short_descriptions': short_descriptions,
     'temperatures': temperatures
     })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
