import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import time

def get_death_count():
    daily_data = open('hourly_data.csv', 'a')
    current_time = datetime.now().strftime("%H:%M:%S")
    url = "https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    divs = soup.find_all('div', {'class': 'big-number'})
    daily_data.write('{},{},{}\n'.format(date.today(), current_time, divs[1].text))
    daily_data.close()

get_death_count()
