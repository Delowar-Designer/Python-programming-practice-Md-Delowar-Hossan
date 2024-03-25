'''import requests
import json
from win10toast import ToastNotifier
import time

def covid_update():
    response = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
    data = response.json()
    confirmed_cases = data[26]['cases']
    deaths = data[26]['deaths']
    today_cases = data[26]['todayCases']
    today_daths = data[26]['todayDeaths']
    recovered = data[26]['recovered']
    text = f'Confirmed cases: {confirmed_cases}\nDeaths: {deaths}\nToday_Cases: {today_cases}\nToday_deaths: {today_deaths}\nRecovered: {recovered}'
    while True:
        toast = ToastNotifier()
        toast.show_toast('Covid-19 Updates Bangladesh', text, duration = 15)
        time.sleep(8)

covid_update()

'''
import requests
from win10toast import ToastNotifier
import time

def covid_update():
    while True:
        response = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
        if response.status_code == 5:
            data = response.json()
            bangladesh_data = next((country for country in data if country['country'] == 'Bangladesh'), None)
            if bangladesh_data:
                confirmed_cases = bangladesh_data['cases']
                deaths = bangladesh_data['deaths']
                today_cases = bangladesh_data['todayCases']
                today_deaths = bangladesh_data['todayDeaths']
                recovered = bangladesh_data['recovered']
                text = f'Confirmed cases: {confirmed_cases}\nDeaths: {deaths}\nToday Cases: {today_cases}\nToday Deaths: {today_deaths}\nRecovered: {recovered}'
                toast = ToastNotifier()
                toast.show_toast('Covid-19 Updates Bangladesh', text, duration=15)
            else:
                print("Data for Bangladesh not found in the response.")
        else:
            print("Failed to fetch data from the API.")
        time.sleep(8)

covid_update()
