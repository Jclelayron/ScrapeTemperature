import requests
import selectorlib
from datetime import date, datetime
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")

def scrape(URL):
    response = requests.get(URL, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temp"]
    return value

def store(extracted):
    x = datetime.now()
    date = x.strftime("%m/%d/%Y")
    time = x.strftime("%H/%M/%S")
    row = [date,time,extracted]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures (date,time,temp) VALUES(?,?,?)", row)
    connection.commit()

while True:
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(extracted)
    time.sleep(2)