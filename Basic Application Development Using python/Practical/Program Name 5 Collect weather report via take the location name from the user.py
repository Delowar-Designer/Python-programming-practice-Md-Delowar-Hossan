# Program Name 5 Collect weather report via take the location name from the user
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace("", "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers = headers)
    print("Searchin...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        print(time)
        print(info)
        print(weather + "C")
    except IndexError:
        print("Weather information not found.")


city = input("Enter the Name of City -> ")
city = city + "weather"
weather(city)
print("Have a Nice Day:)")

# This cod is contributed by adityatri


'''
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")  # Replace spaces with '+' for URL
    res = requests.get(f'https://www.google.com/search?q={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=UTF-8', headers=headers)
    print("Searching..\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dc')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        print(time)
        print(info)
        print(weather + "C")
    except IndexError:
        print("Weather information not found.")

city = input("Enter the Name of City -> ")
city = city + " weather"  # Add a space before 'weather'
weather(city)
print("Have a Nice Day:)")'''
