import os
import requests
import json
import sys
from datetime import date
from datetime import datetime as dt

API_KEY = os.environ.get('NASA_KEY')

URL = "https://api.nasa.gov/planetary/apod"

def fetchAPOD(image_date):
    URL_APOD = URL
    params = {
        'date': image_date,
        'api_key': API_KEY
    }

    if dt.strptime(image_date, "%Y-%m-%d").date() > date.today():
        print("You can't choose dates in the future")
    else: 
        response = requests.get(URL_APOD, params=params)
        data = json.loads(response.text)
        image_title = data['title']
        image_url = data['url']

        # print(f"{image_title}\n{image_url}")
        return image_title, image_url

def main():
    fetchAPOD(sys.argv[1])

if __name__ == "__main__":
    main()
